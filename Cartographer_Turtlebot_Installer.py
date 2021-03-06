#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
if not os.geteuid() == 0:
    sys.exit("""\033[1;91m\n[!] ROS installer must be run as root.\n\033[0m""")

print("""\033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█              Cartographer Turtlebot Installer                █
█                                                              █
└══════════════════════════════════════════════════════════════┘     \033[0m""")

def install():
    global path
    path=raw_input("\033[1;32mplease input the workspace directory>>\033[0m")
    try:
        os.chdir(path)
    except:
        print("\033[1;34m路径出错\033[0m")
        install()
        return
    os.system("apt-get update")
    print("\033[1;34m其他包安装中...\033[0m")
    os.system("sudo apt-get install -y python-wstool python-rosdep ninja-build")
    print("\033[1;34m库安装完毕\033[0m")
    os.chdir(path)
    os.system("mkdir src")
    os.system("echo '# THIS IS AN AUTOGENERATED FILE, LAST GENERATED USING wstool'> src/.rosinstall")
    os.system("echo '- git:'>> src/.rosinstall")
    os.system("echo '    local-name: cartographer'>> src/.rosinstall")
    os.system("echo '    uri: https://github.com/googlecartographer/cartographer.git'>> src/.rosinstall")
    os.system("echo '- git:'>> src/.rosinstall")
    os.system("echo '    local-name: cartographer_ros'>> src/.rosinstall")
    os.system("echo '    uri: https://github.com/googlecartographer/cartographer_ros.git'>> src/.rosinstall")
    os.system("echo '- git:'>> src/.rosinstall")
    os.system("echo '    local-name: cartographer_turtlebot'>> src/.rosinstall")
    os.system("echo '    uri: https://github.com/googlecartographer/cartographer_turtlebot.git'>> src/.rosinstall")
    #os.system("echo '- git:'>> src/.rosinstall")
    #os.system("echo '    local-name: ROS_IMU'>> src/.rosinstall")
    #os.system("echo '    uri: git@github.com:yaozh16/ROS_IMU.git'>> src/.rosinstall")
    os.system("echo '- git:'>> src/.rosinstall")
    os.system("echo '    local-name: ceres-solver'>> src/.rosinstall")
    os.system("echo '    uri: https://github.com/ceres-solver/ceres-solver.git'>> src/.rosinstall")
    #os.system("echo '    version: 1.12.0rc4'>> src/.rosinstall")
    print "\033[1;32mdownloading\033[0m"
    os.system("wstool update -t src")
    try:
        os.system("sudo rosdep init")
    except:
        pass
    os.system("rosdep update")
    print "\033[1;32mTrying to install\033[0m"
    os.system("rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y")
    print "\033[1;32mbuilding\033[0m"
    os.system("catkin_make_isolated --install --use-ninja")
    os.system("source install_isolated/setup.bash")
    print "\033[1;32mFinished\033[0m"
install()
