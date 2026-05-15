#!/usr/bin/env python3
"""
Phase门控检查 - 每个Phase结束必须通过门控才能进入下一Phase
"""

import sys
import os

# 每个Phase的门控条件
PHASE_GATE_CONDITIONS = {
    0: ["需求文档已生成", "用户已确认"],
    1: ["UI设计稿已生成", "用户已确认视觉效果"],
    2: ["数据库表结构已设计", "API文档已生成"],
    3: ["代码可运行", "核心功能已实现"],
    4: ["所有验收标准通过", "截图证据完整"],
    5: ["上线检查清单完成", "监控报警已配置"],
}

def check_phase_gate(phase, evidence_dir="/tmp"):
    """检查指定Phase的门控条件"""
    
    if phase not in PHASE_GATE_CONDITIONS:
        print(f"⚠️ 未知的Phase: {phase}")
        return False
    
    conditions = PHASE_GATE_CONDITIONS[phase]
    print(f"【Phase {phase}门控检查】")
    
    passed = []
    failed = []
    
    # 检查每个条件
    for condition in conditions:
        # 这里简化为检查文件是否存在
        # 实际应该根据条件类型进行不同检查
        condition_file = os.path.join(evidence_dir, f"phase{phase}_{condition.replace(' ', '_')}.txt")
        
        if os.path.exists(condition_file):
            print(f"✅ {condition}")
            passed.append(condition)
        else:
            # 对于用户确认类条件，检查是否有确认记录
            if "用户已确认" in condition:
                confirm_file = os.path.join(evidence_dir, f"phase{phase}_user_confirm.txt")
                if os.path.exists(confirm_file):
                    print(f"✅ {condition}")
                    passed.append(condition)
                else:
                    print(f"❌ {condition}")
                    failed.append(condition)
            else:
                print(f"❌ {condition}")
                failed.append(condition)
    
    if failed:
        print(f"\n❌ Phase {phase}门控未通过：")
        for condition in failed:
            print(f"   - {condition}")
        print(f"\n必须完成以上条件才能进入Phase {phase+1}。")
        return False
    
    print(f"\n✅ Phase {phase}门控通过，可以进入Phase {phase+1}。")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python gate_checker.py --phase=N")
        sys.exit(1)
    
    # 解析参数
    phase_arg = sys.argv[1]
    if phase_arg.startswith("--phase="):
        phase = int(phase_arg.split("=")[1])
    else:
        print(f"❌ 无效参数: {phase_arg}")
        sys.exit(1)
    
    success = check_phase_gate(phase)
    sys.exit(0 if success else 1)