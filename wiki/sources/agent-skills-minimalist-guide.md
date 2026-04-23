---
type: source
title: Agent Skills 极简入门：从零写你的第一个 Skill
date: 2026-03-03
source_url: ""
domain: ""
author: 岱下行者
tags: []
processed: true
raw_file: raw/articles/Agent Skills 极简入门：从零写你的第一个 Skill.md
raw_sha256: ba613fc3688284fc43663aee754003e6954ba50a874ef4f974740948a9511095
last_verified: 2026-04-22
possibly_outdated: false
language: zh
canonical_source: ""
---

## Summary

这篇文章介绍了一个利用 Zotero、NotebookLM 和 Cursor 构建的 AI 辅助学术写作流水线，旨在将碎片化的文献笔记高效转化为逻辑严密的综述初稿。文章详细拆解了由数据“脱水”、逻辑“重构”与全域“编排”三步走策略，强调通过高纯度语料喂养和强约束提示词解决传统写作中手动搬砖感强、逻辑断层及引用混乱等痛点，最终实现人机协作最优配比（AI 完成 70% 体力活，人类贡献 30% 灵魂注入）。

## Key Points

- 核心工具链：Zotero（数据脱水导出 Markdown 笔记）、NotebookLM（横向对比生成逻辑矩阵）、Cursor（关联编辑确保逻辑自洽）
- 三步走策略：1) 数据脱水 - 从 Zotero 导出高纯度笔记；2) 逻辑重构 - 用 NotebookLM 进行多文献横向对比；3) 全域编排 - 在 Cursor 中完成逻辑缝合与初稿生成
- 高纯度语料喂养：强调 AI 生成内容的上限取决于输入语料质量，Zotero 导出的 Notes.md 是经过人工筛选的“精饲料”
- 防 AI 幻觉机制：基于原始标注（Grounding），利用 Cursor 的 @Sources 功能强制 AI 在找不到证据时标注 [Missing]，严禁自行编造
- 人机协作配比：AI 完成框架搭建、数据检索、文献串联和初稿生成等 70% 体力活，人类集中精力于逻辑校对、评判与灵魂注入
- 解决传统痛点：突破线性工具处理网状逻辑的瓶颈，将枯燥写作变为具有“场景感”和“直觉化操作”的高级调优过程

## Concepts Extracted

- [[ai-assisted-academic-writing]]
- [[research-workflow-automation]]
- [[human-ai-collaboration]]
- [[anti-ai-hallucination-techniques]]
- [[literature-synthesis-methods]]

## Entities Extracted

- [[zotero]]
- [[notebooklm]]
- [[cursor]]

## Contradictions

<!-- Disagreements with other sources -->

## My Notes

<!-- Personal notes and reflections -->