#!/usr/bin/env python3
"""
进度追踪器 - 生成可视化进度条
"""

import sys
import json
from datetime import datetime

def generate_progress_bar(current_phase, total_phases=6):
    """生成进度条"""
    
    # Phase名称
    phase_names = {
        -1: "环境检查",
        0: "需求澄清",
        1: "UI设计",
        2: "技术设计",
        3: "开发",
        4: "验证",
        5: "上线",
    }
    
    # 计算进度百分比
    completed_phases = current_phase + 1  # 包括Phase -1
    progress_percent = int((completed_phases / total_phases) * 100)
    
    # 生成进度条
    filled_blocks = int(progress_percent / 10)
    empty_blocks = 10 - filled_blocks
    progress_bar = "█" * filled_blocks + "░" * empty_blocks
    
    # 生成状态列表
    status_lines = []
    for phase in range(-1, 6):
        if phase < current_phase:
            status_lines.append(f"✅ Phase {phase} {phase_names.get(phase, '未知')}（已完成）")
        elif phase == current_phase:
            status_lines.append(f"🔄 Phase {phase} {phase_names.get(phase, '未知')}（进行中）")
        else:
            status_lines.append(f"⏳ Phase {phase} {phase_names.get(phase, '未知')}（待开始）")
    
    # 输出进度报告
    print("【项目进度】")
    print(f"{progress_bar} {progress_percent}% Phase {current_phase} {phase_names.get(current_phase, '进行中')}")
    print()
    for line in status_lines:
        print(line)
    
    return {
        "progress_percent": progress_percent,
        "current_phase": current_phase,
        "completed_phases": completed_phases,
        "total_phases": total_phases,
    }

def save_progress_snapshot(phase, snapshot_dir=".snapshots"):
    """保存Phase快照"""
    
    import os
    os.makedirs(snapshot_dir, exist_ok=True)
    
    snapshot_file = os.path.join(snapshot_dir, f"phase{phase}_snapshot.json")
    
    snapshot = {
        "phase": phase,
        "timestamp": datetime.now().isoformat(),
        "status": "completed",
    }
    
    with open(snapshot_file, 'w') as f:
        json.dump(snapshot, f, indent=2)
    
    print(f"✅ 快照已保存：{snapshot_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # 默认显示当前进度
        print("用法:")
        print("  python progress_tracker.py --phase=N  # 显示进度")
        print("  python progress_tracker.py --save=N   # 保存快照")
        sys.exit(0)
    
    # 解析参数
    arg = sys.argv[1]
    
    if arg.startswith("--phase="):
        phase = int(arg.split("=")[1])
        generate_progress_bar(phase)
    elif arg.startswith("--save="):
        phase = int(arg.split("=")[1])
        save_progress_snapshot(phase)
    else:
        print(f"❌ 无效参数: {arg}")
        sys.exit(1)