---
title: "LLM Wiki 搭建教程 - 飞书云文档"
source: "https://hcn9zwu8a0fz.feishu.cn/wiki/AM3ewXySViopPdkE8Gic90BDnRb"
author:
published:
created: 2026-04-22
description:
tags:
  - "clippings"
---
LLM Wiki 搭建教程

基于 Andrej Karpathy llm-wiki 模式的个人知识库系统。

核心理念：你只负责剪藏，LLM 负责理解和沉淀。

核心思想

与传统 RAG 的根本区别在于，它将知识「编译一次、持续维护」，而非「每次查询时重新推导」。

代码块

你（人类） LLM（知识库管理员）

│ │

│ 剪藏原始来源 │

├───────────────────────────────►│

│ │ 读取、理解、提取

│ │ 编译到 Wiki 层

│ │

│◄───────────────────────────────┤

│ 浏览 Wiki（只读） │（维护所有内容）

核心原则

1.

Raw 层不可变 — 原始来源绝对不修改

2.

Wiki 层 LLM 完全拥有 — 你只浏览，不编辑

3.

输出必须持久化 — 答案写入 outputs/，不消失在对话中

4.

矛盾必须显式标注 — 来源分歧明确记录

5.

每次操作都记日志 — 所有操作写入 wiki/log.md

核心架构分层

评论（1）

跳转至首条评论

0 字

- 帮助中心

- 效率指南

加载中...

当前工作表