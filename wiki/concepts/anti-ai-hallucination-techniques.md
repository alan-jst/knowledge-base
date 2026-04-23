---
type: concept
title: "防 AI 幻觉技术"
date: 2026-04-22
updated: 2026-04-22
tags: []
source_count: 1
confidence: low
domain_volatility: medium
last_reviewed: 2026-04-22
aliases: ["防 AI 幻觉技术", "Anti-AI hallucination techniques"]
---

## Definition
防 AI 幻觉技术（Anti-AI Hallucination Techniques）

## Key Points

- 基于原始标注（Grounding）：所有 AI 输入源都是用户在 Zotero 中的真实笔记，而非让 AI 在互联网上漫无目的地检索
- 强约束防幻觉：利用 Cursor 的 @Sources 功能，强制 AI 在找不到证据时标注 [Missing]，严禁自行编造参考文献
- 确保每一处引用都能对应真实的 Citation Key，建立严密的约束机制
- 解决传统 AI 写作容易编造参考文献的学术安全问题
- 通过高纯度语料喂养（人工筛选的笔记）降低 AI 产生幻觉的概率

## My Position

<!-- Personal position on this concept -->

## Contradictions

<!-- Contradictions between sources about this concept -->

## Sources

- [[agent-skills-minimalist-guide]]

## Evolution Log

- 2026-04-22 (1 source): 页面创建，基于 [[agent-skills-minimalist-guide]] 定义防 AI 幻觉的 grounding 和约束机制