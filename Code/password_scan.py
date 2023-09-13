#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# password_scan.py

import os



class PasswordScan:
    def __init__(self, unix_in, wordlist, unix_out, thread_count):
        self.unix_in = unix_in
        self.wordlist = wordlist
        #self.john_path = john_path
        self.unix_out = unix_out
        self.thread_count = thread_count

    
    def addUserid(self):
        passFiles = os.listdir(self.unix_in)  # 获取输入目录中的文件列表
        
        weak_password = set()  # 用来跟踪已经存在的用户的集合

        with open(self.wordlist, 'a+') as w:
            for line in w:
                weak_password.add(line.strip())
        
            # 遍历输入目录中的密码文件
            for passfile in passFiles:
                with open(os.path.join(self.unix_in, passfile), 'r') as f:
                    for password in f:
                        user = password.split(":", 1)[0]  
                        if user not in weak_password:  
                            w.write(user + "\n")  # 将用户追加到字典中
                            weak_password.add(user)  # 将新用户添加到已集合中



    def brute(self):
        passFiles = os.listdir(self.unix_in)
        for passfile in passFiles:
            john_command = 'john --fork={} --wordlist={} {}'.format(
                #--format=sha512crypt 
                #self.john_path,
                self.thread_count,
                self.wordlist,
                os.path.join(self.unix_in, passfile)
            )

            try:
                os.system('rm -f ~/.john/john.pot')
            except:
                pass
            
            result = os.popen(john_command).read()
            
            # 拆分并删除重复行
            result_lines = result.splitlines()
            unique_results = list(set(result_lines))

            output_file = os.path.join(self.unix_out, passfile)
            with open(output_file, 'w') as f:
                f.write('\n'.join(unique_results))  # 写入输出文件


    def disPlay(self):
        #获取输出目录中所有文件的路径，并存储在 output_files 列表中
        output_files = [os.path.join(self.unix_out, passfile) for passfile in os.listdir(self.unix_out)]
        for output_file in output_files:
            with open(output_file, 'r') as f:
                print("文件'{}'的内容：".format(output_file))
                print("-" * 100)
                print(f.read())
                print("=" * 100)
