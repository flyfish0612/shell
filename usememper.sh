#!/bin/bash
echo "此脚本可以用来查看当前系统的内存使用百分比"
use=$(free -m |grep Mem:|awk '{print $3}')
total=$(free -m|grep Mem:|awk '{print $2}')
useper=$(expr $use \* 100 / $total)
echo "系统当前内存使用百分比为：${useper}%"
