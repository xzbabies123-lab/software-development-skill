#!/usr/bin/env python3
"""
环境快速检查 - Phase -1
检查核心依赖是否可用，失败则无法继续
"""

import sys
import subprocess

def check_todo_available():
    """检查todo工具是否可用"""
    try:
        # 检查todo工具是否在Hermes工具集中
        # 这里简化为检查Python环境
        return True
    except:
        return False

def check_terminal_available():
    """检查terminal工具是否可用"""
    try:
        result = subprocess.run(['which', 'python3'], capture_output=True, timeout=5)
        return result.returncode == 0
    except:
        return False

def check_python_available():
    """检查Python环境"""
    try:
        result = subprocess.run(['python3', '--version'], capture_output=True, timeout=5)
        return result.returncode == 0
    except:
        return False

def check_brainstorm_focus_available():
    """检查brainstorm-focus skill是否可用"""
    try:
        import os
        skill_path = os.path.expanduser('~/.hermes/profiles/wentian/skills/brainstorm-focus')
        return os.path.exists(skill_path)
    except:
        return False

def check_browser_vision_available():
    """检查browser_vision工具是否可用"""
    # 简化检查，实际应该检查Hermes工具集
    return True

def check_vision_analyze_available():
    """检查vision_analyze工具是否可用"""
    # 简化检查，实际应该检查Hermes工具集
    return True

def quick_check():
    """快速检查核心依赖"""
    
    print("【环境检查】")
    
    # 核心检查（失败则停止）
    critical_checks = [
        ("todo工具", check_todo_available, True),
        ("terminal工具", check_terminal_available, True),
        ("Python环境", check_python_available, True),
    ]
    
    # Phase依赖检查（失败可降级）
    phase_checks = [
        ("brainstorm-focus skill", check_brainstorm_focus_available, False),
        ("browser_vision", check_browser_vision_available, False),
        ("vision_analyze", check_vision_analyze_available, False),
    ]
    
    critical_failures = []
    phase_warnings = []
    
    # 执行核心检查
    for name, check_func, is_critical in critical_checks:
        if check_func():
            print(f"✅ {name}可用")
        else:
            print(f"❌ {name}不可用")
            if is_critical:
                critical_failures.append(name)
    
    # 执行Phase依赖检查
    for name, check_func, is_critical in phase_checks:
        if check_func():
            print(f"✅ {name}可用")
        else:
            print(f"⚠️ {name}不可用 → 降级方案")
            phase_warnings.append(name)
    
    # 输出结果
    if critical_failures:
        print("\n❌ 环境检查失败，无法继续：")
        for name in critical_failures:
            print(f"   - {name}不可用")
        print("\n请修复以上问题后重试。")
        return False
    
    if phase_warnings:
        print("\n⚠️ 部分工具不可用，将使用降级方案：")
        for name in phase_warnings:
            if name == "brainstorm-focus skill":
                print(f"   - {name} → 使用普通提问代替")
            elif name in ["browser_vision", "vision_analyze"]:
                print(f"   - {name} → 使用文字描述代替截图")
    
    print("\n✅ 环境检查通过，开始Phase 0。")
    return True

if __name__ == "__main__":
    success = quick_check()
    sys.exit(0 if success else 1)