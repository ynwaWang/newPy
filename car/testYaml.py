#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by David Wang on 16/9/14

import dateexpr as expr
import yaml

class ExcelTemplate(object):
    def __init__(self, config_file):
        self.config_file = config_file
        self.configs = yaml.load(file(self.config_file))
        self.job_name = self.configs['job_name']
        self.params = self.configs.get('job_params', None)
        self.confs = self.configs.get('confs', None)
        self.args = self.configs.get('args', None)
        self.append_file = self.configs.get('append_file', None)
        self.spec = self.configs.get('spec', dict(aligned=True, period='day'))


    def _run_task(self, file_path, params=None, conf=None, args=None):
        import subprocess
        cmd = '/usr/lib/spark-current/bin/spark-submit '

        if params:
            cmd = cmd + ' ' + self._params_to_spark(params)

        if conf:
            cmd = cmd + ' ' + self._confs_to_spark(conf)
        cmd = cmd + ' ' + file_path
        if args:
            cmd = cmd + ' ' + ' '.join(args)
        print(cmd)
        child_process = subprocess.Popen(cmd, shell=True)
        (stdout, stderr) = child_process.communicate()
        returncode = child_process.returncode
        return returncode, stderr, stdout

    def _params_to_spark(self, params_dict):
        kv_pairs = []
        for (k, v) in params_dict.items():
            if k == "jars":
                v = ','.join(v)
            kv_pairs.append("--{k}={v}".format(k=k, v=v))
        return ' '.join(kv_pairs)

    def _confs_to_spark(self, confs_dict):
        return ' --conf ' + ','.join(['{k}={v}'.format(k=k, v=v) for (k, v) in confs_dict.items()])

    def run(self):
        # try:
        #     trans_agent = TransactionAgent(self.job_name, self.spec)
        #     transaction = trans_agent.start()
        # except TaskAreadyDoneException, e:
        #     print(''.join(e.args))
        #     exit(0)

        if self.append_file:
            returncode, stderr, stdout = self._run_task(self.append_file, self.params, self.confs,
                                                        [self.job_name, expr.parse(yaml.safe_dump(self.args))])
        else:
            raise Exception("full_file or append_file must.")

        if returncode:
            raise Exception(stderr, stdout)

            # trans_agent.commit(transaction)


if __name__ == '__main__':
    import sys
    fileName = "E:\\workspace\\wy-data\\deploy\\azkaban_job\\flows\\warehouse_etl_flow\\etl_agg_flow\\spark\\spark_app_report_planbook_daily_excel\\spark_app_report_planbook_daily_excel.yaml"
    # ExcelTemplate(sys.argv[1]).run()
    ExcelTemplate(fileName).run()

