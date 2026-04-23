---
graph-excluded: true
---

# 系统状态核查报告 2026-04-22

## 一、目录结构完整性

验证 raw/ 和 wiki/ 下所有子目录是否存在：

### raw/ 子目录
- ✅ raw/articles/ - 存在
- ✅ raw/clippings/ - 存在
- ✅ raw/images/ - 存在
- ✅ raw/notes/ - 存在
- ✅ raw/pdfs/ - 存在
- ✅ raw/personal/ - 存在

### wiki/ 子目录
- ✅ wiki/concepts/ - 存在
- ✅ wiki/entities/ - 存在
- ✅ wiki/sources/ - 存在
- ✅ wiki/synthesis/ - 存在
- ✅ wiki/templates/ - 存在
- ✅ wiki/outputs/ - 存在

**结论**: ✅ 所有必需目录结构完整

## 二、CLAUDE.md 关键规则覆盖（逐项输出是/否）

- [x] ✅ Raw 层不可变原则 - 第6-12行明确说明
- [x] ✅ INGEST 来源类型判断（personal-writing vs 外部来源） - 第18-23行
- [x] ✅ INGEST SHA-256 哈希记录规则 - 第35-41行
- [ ] ❌ INGEST 去重检测（含 canonical_source 译文检测） - **缺失**：有 canonical_source 字段但无具体检测规则
- [x] ✅ INGEST 概念名称对齐检查（aliases 匹配） - 第43-48行
- [x] ✅ INGEST QUESTIONS.md 匹配检查 - 第59-61行
- [x] ✅ INGEST 缺少 frontmatter 的处理规则 - 第25-30行
- [ ] ❌ INGEST URL 直接输入的 defuddle 调用规则 - **缺失**：未提及 defuddle 工具或 URL 直接输入处理
- [ ] ❌ INGEST 最后一步执行 qmd update - **缺失**：未提及 qmd update 步骤
- [x] ✅ QUERY 使用 qmd query 优先（含 fallback） - 第79行
- [x] ✅ QUERY 来源溯源要求（追溯到 sources 页） - 第83行
- [x] ✅ QUERY Confidence Notes 输出要求 - 第85行
- [x] ✅ QUERY 高价值答案持久化规则 - 第85行
- [x] ✅ confidence: high 必须用户确认，禁止自动晋升 - 第205-206行
- [x] ✅ LINT 运行 scripts/lint.py（9 项检查） - 第101行
- [x] ✅ LINT 执行 qmd 索引同步验证 - 第103行
- [x] ✅ REFLECT Stage 0 反向检验 - 第112行
- [x] ✅ REFLECT Stage 1 使用 qmd multi-get 批量扫描 - 第114-119行
- [x] ✅ REFLECT Stage 3 Gap Analysis - 第124-128行
- [x] ✅ MERGE 跨语言合并专项流程（redirect 文件保留） - 第143-150行
- [x] ✅ Wikilink 格式铁律（英文小写连字符） - 第164-170行
- [x] ✅ Wikilink 禁止清单（系统文件不得被 wikilink） - 第184-189行
- [x] ✅ Wiki 语言规范（中文写作，英文 slug，aliases 跨语言） - 第191-197行
- [x] ✅ 系统文件隔离规则（graph-excluded: true） - 第216-224行
- [ ] ❌ 文档维护规则（CLAUDE.md 更新时同步 USER_GUIDE.md） - **部分缺失**：规则存在（第226-228行），但 USER_GUIDE.md 文件未创建

**总结**: 25项中22项✅通过，3项❌未通过

## 三、模板文件完整性（逐项验证必需字段）

- [x] ✅ source-template.md 含 language / canonical_source - 第14-15行
- [x] ✅ personal-writing-template.md 含 type: personal-writing / confidence_at_writing - 第2、7行
- [x] ✅ concept-template.md 含 aliases / domain_volatility / last_reviewed / Evolution Log - 第9-11、33-36行
- [x] ✅ entity-template.md 含 aliases - 第7行
- [x] ✅ synthesis-template.md 含 Counter-evidence / Confidence Notes / Limitations - 第18-20、26-32行

**结论**: ✅ 所有模板文件字段完整

## 四、系统文件隔离状态

- [x] ✅ wiki/log.md 含 graph-excluded: true - 第3行
- [x] ✅ wiki/index.md 含 graph-excluded: true - 第3行
- [x] ✅ wiki/overview.md 含 graph-excluded: true - 第3行
- [x] ✅ wiki/QUESTIONS.md 含 graph-excluded: true - 第3行

**结论**: ✅ 所有系统文件正确隔离

## 五、scripts/lint.py 检查项

检查项列表（第191-201行）：
1. ✅ YAML frontmatter validity
2. ✅ Broken wikilinks  
3. ✅ Index consistency
4. ✅ Stub pages
5. ✅ Near duplicate concept names
6. ✅ SHA-256 integrity
7. ✅ Stale pages
8. ⚠ Cross-language duplicates（标注"not fully implemented"）
9. ✅ Wikilink format规范

**结论**: ⚠ 9项检查中8项完整实现，1项（跨语言重复）未完全实现

## 六、qmd 状态

### qmd status 输出摘要
- **索引文件数**: 9 files indexed
- **向量嵌入**: 0 embedded, 9 pending（embed 任务失败）
- **集合**: `D:\knowledge-base\wiki` (**/*.md 模式)
- **索引位置**: `D:/cadence_17.4/Cadence/SPB_Data/.cache/qmd/index.sqlite`

### 测试查询结果
1. **向量查询** (`qmd query`): ⚠ 因向量嵌入失败而受阻（qmd embed 任务显示 "fetch failed"）
2. **文本搜索** (`qmd search "knowledge" -n 3`): ✅ 正常工作，返回 top 3 结果：
   - `wiki/log.md` - "Knowledge Base Log"
   - `wiki/questions.md` - "Knowledge Base Questions"  
   - `wiki/index.md` - "Knowledge Base Index"

**结论**: ⚠ 向量搜索功能因嵌入失败不可用，但文本搜索功能正常

## 总结与建议修复优先级

### 总体评估
- **目录结构**: ✅ 完整
- **CLAUDE.md 规则覆盖**: ⚠ 22/25 项通过（87%）
- **模板文件**: ✅ 完整  
- **系统文件隔离**: ✅ 正确
- **lint.py 检查项**: ⚠ 8/9 项完整实现（89%）
- **qmd 集成**: ⚠ 文本搜索正常，向量搜索失败

### 建议修复优先级

#### 🔴 高优先级（影响核心功能）
1. **qmd embed 失败** - 向量搜索不可用，影响 QUERY 和 REFLECT 操作
   - 可能原因：网络连接、模型下载、GPU 驱动问题
   - 建议：检查网络，尝试 `qmd embed --help` 查看选项

2. **USER_GUIDE.md 缺失** - CLAUDE.md 要求同步但文件不存在
   - 建议：创建 USER_GUIDE.md 或从 CLAUDE.md 移除该要求

#### 🟡 中优先级（规则完整性）
3. **CLAUDE.md 缺失规则**（3项）：
   - INGEST 去重检测（含 canonical_source 译文检测）
   - INGEST URL 直接输入的 defuddle 调用规则
   - INGEST 最后一步执行 qmd update
   - 建议：补充缺失规则到 CLAUDE.md

4. **lint.py 跨语言重复检查未实现**
   - 建议：完善 check8_cross_language_duplicates() 函数

#### 🟢 低优先级（优化改进）
5. **文档一致性** - 确保所有文档与 CLAUDE.md 规则一致
6. **测试数据** - 添加示例数据验证完整工作流

### 最终状态
**系统基本框架**: ✅ 已建立  
**核心功能就绪**: ⚠ 部分功能需要修复  
**生产可用性**: 🔴 需要先解决高优先级问题

