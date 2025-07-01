# Point-in-Time Large Language Models

## Overview
This document lists various projects and resources related to Point-in-Time (chronologically consistent) Large Language Models.

## Presentation
- [Point-in-Time LLMs Overview Presentation](https://docs.google.com/presentation/d/1i1U31CBO-HXjv8Ypp9kdsJxQIiJKfB_zE5S-0MWVa_0/edit?usp=sharing)

## Major Open-Source Model Sequences
The following projects provide sequences of ≥10 date-stamped LLM checkpoints, each trained only on data available up to its cut-off. All include Python loaders or training scripts and are actively maintained.

### 1. TimeLMs
- **Project**: [cardiffnlp/timelms](https://github.com/cardiffnlp/timelms)
- **Coverage**: 2019-Q4 → 2022-Q4 (18 RoBERTa-base checkpoints, quarterly)
- **Model**: RoBERTa-base
- **Purpose**: Diachronic Twitter analysis & degradation studies
- **Status**: Widely cited, actively maintained

### 2. ChronoBERT / ChronoGPT
- **Project**: [manelalab/chrono-bert-v1-YYYY1231](https://huggingface.co/collections/manelalab/chronobert-67c1ca6c2382e03aaec446f8)
- **Coverage**: 1999-2024 (26 yearly BERT-base and GPT-2-medium checkpoints)
- **Models**: BERT-base / GPT-2
- **Purpose**: Look-ahead–free language understanding & finance return-forecasting
- **Status**: Widely cited, actively maintained
- **Resources**: 
  - [Paper](https://arxiv.org/abs/2502.21206)
  - [Hugging Face Collection](https://huggingface.co/collections/manelalab/chronobert-67c1ca6c2382e03aaec446f8)

### 3. StoriesLM
- **Project**: [StoriesLM/StoriesLM-v1-YYYY](https://huggingface.co/StoriesLM/StoriesLM-v1-1963)
- **Coverage**: 1900-1963 (64 yearly checkpoints)
- **Model**: BERT-base
- **Purpose**: Historical newspaper language; cultural-shift research
- **Status**: Widely cited, actively maintained

### 4. HistBERT
- **Project**: [wendyqiu/diachronicBert](https://github.com/wendyqiu/diachronicBert)
- **Coverage**: 1900s → 2000s (10 decade-wise checkpoints)
- **Model**: BERT-base
- **Purpose**: Diachronic lexical-semantic change in COHA corpus
- **Status**: Widely cited, actively maintained

## Related Projects and Research

### Benchmarks and Tools
- [ChroKnowledge](https://p-yi.github.io/ChroKnowledge/) - Benchmark for chronological knowledge
- [FinGPT](https://arxiv.org/abs/2306.06031) - Toolkit for continuous learning
- [TemporalWiki](https://arxiv.org/abs/2204.14211) - [GitHub Repository](https://github.com/joeljang/temporalwiki/tree/main)

### Research Papers
#### Temporal Language Understanding
- [Streaming LLM](https://arxiv.org/abs/2102.01951) - Efficient processing of streaming text data
- [Time-Aware LLM as Temporal Knowledge Bases](https://arxiv.org/abs/2106.15110) - Using LLMs for temporal knowledge representation
- [Temporal Knowledge Graph Completion](https://arxiv.org/abs/2101.02613) - Methods for temporal knowledge graph reasoning
- [Temporal Language Models for Historical Text Analysis](https://arxiv.org/abs/2203.08474) - Analysis of historical language patterns

#### Applications and Use Cases
- [Temporal Question Answering](https://arxiv.org/abs/2205.08184) - Methods for answering time-sensitive questions
- [Historical Event Extraction](https://arxiv.org/abs/2204.14211) - Extracting and analyzing historical events
- [Temporal Information Extraction](https://arxiv.org/abs/2109.03241) - Extracting temporal information from text
- [Diachronic Word Embeddings](https://arxiv.org/abs/2103.06454) - Tracking word meaning changes over time

#### Technical Approaches
- [Temporal Pre-training](https://arxiv.org/abs/2104.08685) - Pre-training methods for temporal understanding
- [Temporal Fine-tuning](https://arxiv.org/abs/2105.03023) - Fine-tuning approaches for temporal tasks
- [Temporal Evaluation](https://arxiv.org/abs/2106.15110) - Evaluation metrics for temporal language models
- [Temporal Data Augmentation](https://arxiv.org/abs/2107.03051) - Data augmentation techniques for temporal tasks

### Datasets and Resources
- [TemporalWiki](https://github.com/joeljang/temporalwiki) - Temporal knowledge graph dataset
- [ChroKnowledge](https://p-yi.github.io/ChroKnowledge/) - Benchmark for chronological knowledge
- [Historical News Archives](https://github.com/StoriesLM) - Historical newspaper datasets
- [Temporal Question Answering Datasets](https://github.com/temporal-qa) - Datasets for temporal QA tasks

### Tools and Frameworks
- [FinGPT](https://github.com/fingpt) - Financial temporal analysis toolkit
- [TemporalNLP](https://github.com/temporal-nlp) - NLP tools for temporal analysis
- [ChronoBERT](https://github.com/chronobert) - Framework for temporal language modeling
- [TimeLM](https://github.com/cardiffnlp/timelms) - Tools for temporal language model analysis 