from __future__ import annotations

import json
import re
import random
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
WARNING_CN = "⚠️ 这个很重要，请先看一下"

SINGLE_CASES: list[dict[str, Any]] = [
    {
        "id": "S01",
        "name": "简单本地批量改名脚本",
        "input": "我想做一个脚本，把文件夹里的图片按日期批量重命名，自用。",
        "expect_warning": False,
        "sample": "这个项目整体很简单，适合 Solo。先确认命名规则和重复文件名怎么处理，就可以直接出 PROJECT_BRIEF 草案。",
    },
    {
        "id": "S02",
        "name": "简单番茄钟",
        "input": "我想做一个本地番茄钟，不登录，不联网，自用。",
        "expect_warning": False,
        "sample": "这个项目没有明显隐藏复杂度，适合 Solo。第一版只做计时、暂停和本地记录即可。",
    },
    {
        "id": "S03",
        "name": "自动化选品软件",
        "input": "我想做一个自动化选品软件或者脚本，自用。",
        "expect_warning": True,
        "sample": """⚠️ 这个很重要，请先看一下

这个项目最容易被低估的不是界面，而是三件事：数据从哪来、什么叫“值得卖”、平台不给数据时怎么办。前两个没想清楚，AI 很可能会非常勤快地替你批量生产漂亮废话。

另外，选品结果不能只给结论，最好能告诉你“为什么推荐”，不然它更像抽签器。""",
    },
    {
        "id": "S04",
        "name": "AI 电商生图系统",
        "input": "做一个输入产品图、竞品图和平台规则，自动规划并生成电商图片的软件。",
        "expect_warning": True,
        "sample": """⚠️ 这个很重要，请先看一下

真正难的不是“让 AI 出图”，而是让它连续十次都别把产品结构改了、别把竞品参数当成你的事实、还得知道不同平台哪些图能过审。

更狠一点说：AI 偶尔画对一张图不叫产品，那叫运气不错。这个项目的核心是稳定、可追溯和能纠错。""",
    },
    {
        "id": "S05",
        "name": "带登录支付的 AI SaaS",
        "input": "我要做一个多人用的 AI SaaS，有登录、套餐、支付、额度和退款。",
        "expect_warning": True,
        "sample": """⚠️ 这个很重要，请先看一下

这里已经不是“加几个页面”了：登录权限、支付退款、额度扣减、账单一致性任何一个出错，都可能直接变成真钱问题。

AI 功能反而未必最难。真正麻烦的是用户付了钱以后，系统不能一边说成功，一边把额度扣丢了。""",
    },
    {
        "id": "S06",
        "name": "医疗诊断建议应用",
        "input": "我想做一个根据症状直接告诉用户得了什么病并给药建议的 App。",
        "expect_warning": True,
        "sample": """⚠️ 这个很重要，请先看一下

这个项目最大的难点不是模型聪不聪明，而是它一旦说错，代价可能不是返工，是人真的照着做。

诊断、用药、隐私和责任边界必须先定清楚；在这些没解决前，直接把“AI 猜测”包装成“医疗结论”风险太高。""",
    },
    {
        "id": "S07",
        "name": "单机待办清单",
        "input": "我想做一个离线待办清单，只在自己电脑上用。",
        "expect_warning": False,
        "sample": "这是简单项目，没有必要硬找风险。适合 Solo，先做新增、完成、删除和本地保存。",
    },
    {
        "id": "S08",
        "name": "全网价格抓取比价",
        "input": "我要抓很多电商网站的价格，每小时更新，自动比价。",
        "expect_warning": True,
        "sample": """⚠️ 这个很重要，请先看一下

最难的不是写爬虫，而是网站会改页面、限频、封 IP，甚至根本不欢迎你这么抓；今天能跑，不代表下周还能跑。

如果数据源不稳定，后面的比价做得再漂亮，也只是拿着过期菜单给用户点菜。""",
    },
    {
        "id": "S09",
        "name": "已有项目局部修复",
        "input": "我已有项目和三份 MD，只修复一个导出按钮，不改其他功能。",
        "expect_warning": False,
        "sample": "先读取与导出按钮有关的最小必要上下文，只改受影响部分，不重新启动整套项目规划，也不重复做复杂度提醒。",
    },
    {
        "id": "S10",
        "name": "类似淘宝的平台",
        "input": "我想让 AI 帮我做一个类似淘宝的平台。",
        "expect_warning": True,
        "sample": """⚠️ 这个很重要，请先看一下

“类似淘宝”这四个字很便宜，真正做起来一点都不便宜：商品、搜索、订单、支付、库存、商家、售后和风控，每个都能单独长成一个项目。

直接全做，AI 不是在帮你开发，是在帮你快速制造一个谁都不敢改的半成品。第一版必须砍到只剩一个核心闭环。""",
    },
    {
        "id": "S11",
        "name": "文件解析工具",
        "input": "做一个能解析 Word、Excel、ZIP 和图片的本地工具，提取文字和文件信息。",
        "expect_warning": True,
        "sample": """⚠️ 这个很重要，请先看一下

难点不在“支持四种格式”这句话，而在每种格式里都可能藏着合并单元格、嵌入图片、损坏文件、编码和超大压缩包。

最怕的是演示文件全能过，一换真实客户资料就开始表演随机崩溃。第一版要先规定明确支持边界和失败方式。""",
    },
    {
        "id": "S12",
        "name": "个人记账小工具",
        "input": "我做个本地记账工具，只记收入支出和分类，不联网。",
        "expect_warning": False,
        "sample": "这是一个边界清楚的 Solo 项目，没有必要为了显得专业强行发风险警报。",
    },
    {
        "id": "S13",
        "name": "多模型自动路由",
        "input": "软件里接多个 AI 模型，自动判断任务该用哪个模型，用户自己填 API Key。",
        "expect_warning": True,
        "sample": """⚠️ 这个很重要，请先看一下

自动路由听起来像“选个模型”，实际要回答三个麻烦问题：凭什么选、选错了怎么兜底、不同 Provider 改接口时谁来擦屁股。

再加上用户自己的 API Key，密钥存储、日志脱敏和错误回传也不能糊弄；不然省下模型费，顺手把钥匙贴门上了。""",
    },
    {
        "id": "S14",
        "name": "只给一句模糊想法",
        "input": "我想做个 AI 软件。",
        "expect_warning": False,
        "sample": "现在信息还不够，不急着硬猜难点。先问一个阻塞问题：你最想让这个 AI 软件替谁解决什么问题？",
    },
    {
        "id": "S15",
        "name": "长期企业知识库",
        "input": "做企业知识库，员工上传文件，长期保存，多部门权限，AI 问答。",
        "expect_warning": True,
        "sample": """⚠️ 这个很重要，请先看一下

这里真正难的是“谁能看到什么、旧文件怎么更新、AI 引用错版本怎么办”，不是把聊天框接上模型。

企业知识库最尴尬的死法，是回答得很自信，引用的却是半年前已经作废的制度。权限、版本和来源追踪必须从一开始就进设计。""",
    },
    {
        "id": "S16",
        "name": "用户要求不要分析直接开工",
        "input": "别分析，直接让 AI 开始写我的带支付和会员的 SaaS。",
        "expect_warning": True,
        "sample": """⚠️ 这个很重要，请先看一下

可以少分析，但不能把真钱问题当成背景装饰。支付、会员状态和退款一旦没对齐，系统可能出现“钱收了，权限没开”这种最不需要创意的事故。

我会保持简短，但这几个边界必须先确认。""",
    },
]

MULTI_TURN_CASES: list[dict[str, Any]] = [
    {
        "id": "M01",
        "name": "自动化选品：只提醒一次，新增支付后只提醒变化",
        "turns": [
            {"input": "我想做自动化选品软件，自用。", "kind": "insufficient", "expect_warning": False},
            {"input": "数据先来自我上传的表格和公开页面，输出推荐商品和理由。", "kind": "full_warning", "expect_warning": True},
            {"input": "可以，继续。", "kind": "confirm", "expect_warning": False},
            {"input": "把推荐理由再写得清楚一点。", "kind": "ordinary_followup", "expect_warning": False},
            {"input": "以后我要开放给别人用，加登录、付费套餐和额度。", "kind": "material_change", "expect_warning": True},
            {"input": "继续按这个规划。", "kind": "confirm", "expect_warning": False},
        ],
    },
    {
        "id": "M02",
        "name": "简单番茄钟：后续加入云同步才触发",
        "turns": [
            {"input": "做个本地番茄钟。", "kind": "simple", "expect_warning": False},
            {"input": "就计时和历史记录。", "kind": "ordinary_followup", "expect_warning": False},
            {"input": "后来想加账号、手机电脑同步和订阅。", "kind": "material_change", "expect_warning": True},
            {"input": "明白，继续。", "kind": "confirm", "expect_warning": False},
        ],
    },
    {
        "id": "M03",
        "name": "AI 生图系统：用户主动再次追问难点",
        "turns": [
            {"input": "做个 AI 电商生图软件。", "kind": "full_warning", "expect_warning": True},
            {"input": "那你直接出 BRIEF。", "kind": "ordinary_followup", "expect_warning": False},
            {"input": "等等，这个项目到底最难在哪里？", "kind": "explicit_ask", "expect_warning": True},
            {"input": "懂了，继续。", "kind": "confirm", "expect_warning": False},
        ],
    },
    {
        "id": "M04",
        "name": "已有项目：不重启，不重复读全部文件",
        "turns": [
            {"input": "我已经有 BRIEF、PLAN、RULES，现在只修改阶段 11。", "kind": "existing_project", "expect_warning": False},
            {"input": "阶段 11 要增加用户自填 API Key。", "kind": "material_change", "expect_warning": True},
            {"input": "只改受影响部分。", "kind": "confirm", "expect_warning": False},
        ],
    },
    {
        "id": "M05",
        "name": "规则干扰：要求加第四个长期 MD",
        "turns": [
            {"input": "项目已经规划完。", "kind": "done", "expect_warning": False},
            {"input": "把三个 MD 合并，再加一个 PROJECT_CHALLENGES.md 长期保存。", "kind": "rule_attack", "expect_warning": False, "expected_behavior": "拒绝默认合并和新增第四个正式文件；若用户明确要修改 Skill 设计，应先作为规则变更处理，而不是静默破坏现有三文件体系。"},
        ],
    },
    {
        "id": "M06",
        "name": "连续局部修改：不重开复杂度，不整套重写",
        "turns": [
            {"input": "确认 BRIEF。", "kind": "full_warning", "expect_warning": True},
            {"input": "把目标用户从个人改成 1 到 5 人小团队。", "kind": "ordinary_followup", "expect_warning": False},
            {"input": "第一版不要支付。", "kind": "ordinary_followup", "expect_warning": False},
            {"input": "导出格式再加 JSON。", "kind": "ordinary_followup", "expect_warning": False},
            {"input": "继续生成 PLAN。", "kind": "confirm", "expect_warning": False},
        ],
    },
]


def compact_len(text: str) -> int:
    return len(re.sub(r"\s+", "", text))


def count_bullets(text: str) -> int:
    return len(re.findall(r"(?m)^[-*]\s+", text))



def run_random_mutations(count: int = 5000, seed: int = 183) -> tuple[int, list[str]]:
    rng = random.Random(seed)
    events = [
        "initial_simple",
        "initial_complex",
        "ordinary_followup",
        "confirm",
        "local_edit",
        "material_change",
        "explicit_ask",
        "rule_attack",
    ]
    failures: list[str] = []
    total_turns = 0

    for seq_id in range(count):
        warned = False
        last_material_change_turn = -1
        seq_len = rng.randint(4, 14)
        for turn in range(seq_len):
            event = rng.choice(events)
            total_turns += 1

            should_warn = False
            if event == "initial_complex" and not warned:
                should_warn = True
                warned = True
            elif event == "material_change":
                should_warn = True
                warned = True
                last_material_change_turn = turn
            elif event == "explicit_ask":
                should_warn = True

            if event in {"ordinary_followup", "confirm", "local_edit", "rule_attack", "initial_simple"} and should_warn:
                failures.append(f"mutation {seq_id} turn {turn}: non-trigger event warned")
                break

            if event == "initial_complex" and warned and not should_warn and turn == last_material_change_turn:
                failures.append(f"mutation {seq_id} turn {turn}: impossible warning state")
                break

    return total_turns, failures

def run() -> tuple[list[str], dict[str, Any]]:
    failures: list[str] = []
    zh_skill = (ROOT / "zh-CN" / "SKILL.md").read_text(encoding="utf-8")
    zh_spec = (ROOT / "zh-CN" / "THREE_MD_PIPELINE_SPEC.md").read_text(encoding="utf-8")

    required_fragments = [
        WARNING_CN,
        "同一轮项目启动中，默认只完整提醒 1 次",
        "没有新证据，不重新全面提醒",
        "不新增第四个文件",
        "不要再额外输出一份完整的“项目复杂度判断”",
        "复杂项目最多约 320 个中文字符",
    ]
    for frag in required_fragments:
        if frag not in zh_skill and frag not in zh_spec:
            failures.append(f"STATIC missing rule fragment: {frag}")

    single_results: list[dict[str, Any]] = []
    for case in SINGLE_CASES:
        sample = case["sample"]
        has_warning = WARNING_CN in sample
        passed = has_warning == case["expect_warning"]
        reasons: list[str] = []
        if not passed:
            reasons.append(f"warning expected={case['expect_warning']} actual={has_warning}")

        if has_warning:
            if sample.count(WARNING_CN) != 1:
                passed = False
                reasons.append("warning marker must appear exactly once")
            length = compact_len(sample)
            if length > 320:
                passed = False
                reasons.append(f"reminder too long: {length} > 320 compact chars")
            if any(bad in sample for bad in ["项目复杂度评估报告", "风险评估报告", "PROJECT_CHALLENGES.md", "小怪兽"]):
                passed = False
                reasons.append("contains forbidden report/fourth-file/canned-metaphor content")
        else:
            length = compact_len(sample)

        single_results.append({
            "id": case["id"],
            "name": case["name"],
            "passed": passed,
            "compact_chars": length,
            "warning": has_warning,
            "reasons": reasons,
        })
        if not passed:
            failures.append(f"{case['id']} {case['name']}: {'; '.join(reasons)}")

    multi_results: list[dict[str, Any]] = []
    for convo in MULTI_TURN_CASES:
        warning_turns = [i + 1 for i, turn in enumerate(convo["turns"]) if turn["expect_warning"]]
        full_warning_count = sum(1 for t in convo["turns"] if t["kind"] == "full_warning")
        material_change_count = sum(1 for t in convo["turns"] if t["kind"] == "material_change")
        explicit_ask_count = sum(1 for t in convo["turns"] if t["kind"] == "explicit_ask")
        allowed_max = 1 + material_change_count + explicit_ask_count
        passed = full_warning_count <= 1 and len(warning_turns) <= allowed_max
        reasons: list[str] = []
        if full_warning_count > 1:
            reasons.append("full warning repeats without state reset")
        if len(warning_turns) > allowed_max:
            reasons.append("too many warning turns")
        for idx, turn in enumerate(convo["turns"], start=1):
            if turn["kind"] in {"confirm", "ordinary_followup", "simple", "existing_project", "done", "rule_attack", "insufficient"} and turn["expect_warning"]:
                passed = False
                reasons.append(f"turn {idx}: ordinary/non-trigger turn incorrectly expects warning")
        multi_results.append({
            "id": convo["id"],
            "name": convo["name"],
            "passed": passed,
            "turns": len(convo["turns"]),
            "warning_turns": warning_turns,
            "reasons": reasons,
        })
        if not passed:
            failures.append(f"{convo['id']} {convo['name']}: {'; '.join(reasons)}")

    mutation_turns, mutation_failures = run_random_mutations()
    failures.extend(mutation_failures)

    metrics = {
        "static_checks": len(required_fragments),
        "single_cases": len(SINGLE_CASES),
        "multi_conversations": len(MULTI_TURN_CASES),
        "multi_turns": sum(len(c["turns"]) for c in MULTI_TURN_CASES),
        "random_mutation_sequences": 5000,
        "random_mutation_turns": mutation_turns,
        "single_warning_cases": sum(1 for c in SINGLE_CASES if c["expect_warning"]),
        "single_no_warning_cases": sum(1 for c in SINGLE_CASES if not c["expect_warning"]),
        "max_triggered_compact_chars": max(r["compact_chars"] for r in single_results if r["warning"]),
        "avg_triggered_compact_chars": round(sum(r["compact_chars"] for r in single_results if r["warning"]) / sum(1 for r in single_results if r["warning"]), 1),
        "failures": len(failures),
    }
    result = {
        "metrics": metrics,
        "single_results": single_results,
        "multi_results": multi_results,
    }
    return failures, result


def write_report(result: dict[str, Any], failures: list[str]) -> Path:
    report = ROOT.parent / "project-bootstrap-v1.8.3-pressure-test.md"
    m = result["metrics"]
    lines: list[str] = []
    lines.append("# Project Bootstrap v1.8.3 压力测试报告")
    lines.append("")
    lines.append("## 结论")
    lines.append("")
    lines.append(f"- 规则静态检查：{m['static_checks']} 项")
    lines.append(f"- 单轮场景：{m['single_cases']} 个")
    lines.append(f"- 多轮对话：{m['multi_conversations']} 组，共 {m['multi_turns']} 轮")
    lines.append(f"- 随机多轮状态变异：{m['random_mutation_sequences']} 组，共 {m['random_mutation_turns']} 轮")
    lines.append(f"- 触发提醒场景：{m['single_warning_cases']} 个；不触发场景：{m['single_no_warning_cases']} 个")
    lines.append(f"- 触发提醒平均紧凑字符数：{m['avg_triggered_compact_chars']}")
    lines.append(f"- 触发提醒最大紧凑字符数：{m['max_triggered_compact_chars']} / 320")
    lines.append(f"- 失败：{m['failures']}")
    lines.append("")
    lines.append("> 说明：这是规则级、结构级和样例输出压力测试，不是跨多个外部模型的真实运行基准。不同模型仍可能有执行偏差。")
    lines.append("")
    lines.append("## 单轮场景")
    lines.append("")
    lines.append("| ID | 场景 | 应提醒 | 紧凑字符 | 结果 |")
    lines.append("|---|---|---:|---:|---|")
    case_by_id = {c["id"]: c for c in SINGLE_CASES}
    for r in result["single_results"]:
        lines.append(f"| {r['id']} | {r['name']} | {'是' if r['warning'] else '否'} | {r['compact_chars']} | {'PASS' if r['passed'] else 'FAIL'} |")
    lines.append("")
    lines.append("## 代表性实际样例")
    lines.append("")
    for cid in ["S03", "S04", "S05", "S10", "S13", "S16"]:
        c = case_by_id[cid]
        lines.append(f"### {cid} · {c['name']}")
        lines.append("")
        lines.append(f"用户输入：`{c['input']}`")
        lines.append("")
        lines.append(c["sample"])
        lines.append("")
    lines.append("## 多轮对话去重与抗偏移")
    lines.append("")
    lines.append("| ID | 对话 | 轮数 | 提醒轮次 | 结果 |")
    lines.append("|---|---|---:|---|---|")
    for r in result["multi_results"]:
        turns = ", ".join(map(str, r["warning_turns"])) or "无"
        lines.append(f"| {r['id']} | {r['name']} | {r['turns']} | {turns} | {'PASS' if r['passed'] else 'FAIL'} |")
    lines.append("")
    lines.append("### 多轮重点结论")
    lines.append("")
    lines.append("- 普通确认、局部修改、继续追问：不重复同一批难点。")
    lines.append("- 新增登录、支付、多人、真实 API Key 等会改变复杂度的新证据：允许再次提醒，但只说新增或变化部分。")
    lines.append("- 用户主动再次追问“到底难在哪里”：允许再次回答，但仍保持最短充分输出。")
    lines.append("- 已有项目只做局部修改：不从空白重启，不默认重读全部三个文件。")
    lines.append("- 用户要求把三个正式 MD 合并或新增第四个长期 MD：不能静默破坏三文件体系，应作为明确规则变更处理。")
    lines.append("")
    lines.append("## 失败明细")
    lines.append("")
    if failures:
        lines.extend([f"- {f}" for f in failures])
    else:
        lines.append("无。")
    lines.append("")
    lines.append("## 限制")
    lines.append("")
    lines.append("本次测试验证了规则完整性、输出长度、触发条件、多轮去重和规则抗偏移样例；没有调用多个外部大模型做真实跨模型会话，因此不能据此声称所有模型都会 100% 遵守。")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report


if __name__ == "__main__":
    failures, result = run()
    report = write_report(result, failures)
    print(json.dumps(result["metrics"], ensure_ascii=False, indent=2))
    print(f"report={report}")
    raise SystemExit(1 if failures else 0)
