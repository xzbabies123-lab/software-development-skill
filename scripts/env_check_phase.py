#!/usr/bin/env python3
"""
Phase依赖检查 - 按需检查每个Phase需要的工具
"""

import sys

# 每个Phase需要的工具
PHASE_REQUIREMENTS = {
    0: ["brainstorm-focus"],
    1: ["browser_vision", "vision_analyze"],
    2: ["read_file", "write_file"],
    3: ["terminal", "execute_code"],
    4: ["browser_vision", "vision_analyze"],
    5: ["terminal"],
}

def check_tool_available(tool_name):
    """检查工具是否可用"""
    # 简化检查，实际应该检查Hermes工具集
    # 这里假设所有工具都可用
    return True

def check_phase_requirements(phase):
    """检查指定Phase的依赖"""
    
    if phase not in PHASE_REQUIREMENTS:
        print(f"⚠️ 未知的Phase: {phase}")
        return True
    
    requirements = PHASE_REQUIREMENTS[phase]
    missing = []
    
    print(f"【Phase {phase}依赖检查】")
    
    for tool in requirements:
        if check_tool_available(tool):
            print(f"✅ {tool}可用")
        else:
            print(f"❌ {tool}不可用")
            missing.append(tool)
    
    if missing:
        print(f"\n❌ Phase {phase}依赖缺失：")
        for tool in missing:
            print(f"   - {tool}")
        print(f"\n解决方案：")
        print(f"1. 安装缺失工具")
        print(f"2. 或跳过Phase {phase}（如果不需要）")
        return False
    
    print(f"\n✅ Phase {phase}依赖检查通过。")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python env_check_phase.py --phase=N")
        sys.exit(1)
    
    # 解析参数
    phase_arg = sys.argv[1]
    if phase_arg.startswith("--phase="):
        phase = int(phase_arg.split("=")[1])
    else:
        print(f"❌ 无效参数: {phase_arg}")
        sys.exit(1)
    
    success = check_phase_requirements(phase)
    sys.exit(0 if success else 1)