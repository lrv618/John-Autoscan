#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# main.py

import os

from ascii_art import ascii_art_1, ascii_art_2, ascii_art_3
from password_scan import PasswordScan

def main():
    print("-" * 70)
    print(ascii_art_1)
    print("-" * 70)
    #john_path = '/home/Auto/john/run/john'
    
    while True:                        
        unix_in = input("输入密码文件目录 (默认为 './in'): ").strip() or './in'
        if os.path.isdir(unix_in):
            if os.path.exists(unix_in):
                print("[*]密码文件目录:", unix_in)
                print("-" * 70)
                break
            else:
                print("输入的路径不存在，请重新输入。")
        else:
            print("输入的路径不是一个有效的目录，请重新输入。")


    while True:
        wordlist = input("输入字典文件位置 (默认为 './direction.txt'): ").strip() or './direction.txt'
        if os.path.isfile(wordlist):
            if os.path.exists(wordlist):
                print("[*]字典文件位置:", wordlist)
                print("-" * 70)
                break
            else:
                print("输入的路径不存在，请重新输入。")
        else:
            print("输入的路径不是一个有效的文件，请重新输入。")


    while True:
        unix_out = input("输入输出文件路径 (默认为 './out'): ").strip() or './out'
        if not os.path.exists(unix_out):
            try:
                os.makedirs(unix_out)
                print("[*]创建输出文件路径:", unix_out)
                print("-" * 70)
                break
            except Exception as e:
                print("无法创建输出文件路径:", e)
                print("-" * 70)
        elif os.path.exists(unix_out) and os.path.isdir(unix_out):
            print("[*]输出文件路径:", unix_out)
            print("-" * 70)
            break
        else:
            print("输入的路径不是一个有效的目录，请重新输入。")


    while True:
        try:
            thread_count = int(input("请输入线程数 (默认为 2): ") or 2)
            if thread_count > 0:
                print("-" * 70)
                break
            else:
                print("线程数必须大于0，请重新输入。")
        except ValueError:
            print("无效的输入，请输入一个整数。")


    confirm = input("是否要执行脚本？(y/n): ").lower()
    print("-" * 70)

    if confirm == 'y':
        cracker = PasswordScan(unix_in, wordlist, unix_out, thread_count)
        cracker.addUserid()
        cracker.brute()
        print("-" * 100)
        print(ascii_art_3)
        cracker.disPlay()  # 显示输出文件的内容
        print(ascii_art_2)
    elif confirm == 'n':
        print("脚本已取消。")
    else:
        print("无效的输入。请输入 'y' 继续或 'n' 取消。")


    
if __name__ == '__main__':
    main()