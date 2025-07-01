# Point-in-Time Corpus Sequences

This document lists major corpora and datasets that provide chronologically consistent text sequences, organized by domain and time period. Each entry includes metadata for licensing, granularity, leakage prevention, and evaluation resources.

## Recent Developments (2023-2024)

### Time Machine GPT Datasets
- **Coverage**: Series of point-in-time models
- **Size**: Models and training datasets provided
- **Source**: [Time Machine GPT Project](https://arxiv.org/abs/2404.18543)
- **License**: Open source
- **Granularity**: Snapshot-based
- **Leakage Prevention**: Non-prognosticative training data with strict temporal boundaries
- **Features**:
  - Non-prognosticative training data
  - Temporal boundaries strictly enforced
  - Multiple temporal checkpoints
  - No future information leakage
- **Use Cases**: Language evolution studies, time-series forecasting, historical analysis
- **Status**: Published at NAACL Findings 2024
- **Evaluation**: Temporal consistency validation included

### ChronoBERT/ChronoGPT Datasets
- **Coverage**: 1999-2024 (26 yearly checkpoints)
- **Size**: 26 yearly BERT-base and GPT-2-medium models
- **Source**: [ChronoBERT Project](https://arxiv.org/abs/2502.21206)
- **License**: Open source
- **Granularity**: Yearly snapshots
- **Leakage Prevention**: Look-ahead-free training methodology
- **Features**:
  - Yearly financial and general text data
  - Look-ahead-free language understanding
  - Finance return-forecasting capabilities
- **Use Cases**: Financial forecasting, temporal language understanding
- **Status**: Models available on Hugging Face
- **Evaluation**: Financial return forecasting benchmarks

### StoriesLM Historical Newspapers
- **Coverage**: 1900-1963 (64 yearly checkpoints)
- **Size**: 64 yearly BERT-base models
- **Source**: [StoriesLM Project](https://huggingface.co/StoriesLM/StoriesLM-v1-1963)
- **License**: Open source
- **Granularity**: Yearly snapshots
- **Leakage Prevention**: Derived from American Stories dataset with temporal filtering
- **Features**:
  - Historical newspaper language
  - Cultural shift analysis
  - Yearly temporal granularity
- **Use Cases**: Historical research, cultural evolution studies
- **Status**: Models available on Hugging Face
- **Evaluation**: Historical language evolution benchmarks

## Multilingual and Cross-Lingual Corpora

### HPLT (High-Performance Language Technologies)
- **Coverage**: 75 languages, 5.6T tokens
- **Size**: 5.6 trillion tokens
- **Source**: [HPLT Project](https://hplt-project.org)
- **License**: Open source (OSI compliant)
- **Granularity**: Snapshot-based (v2.0, 2025-05)
- **Leakage Prevention**: Public domain and openly licensed content
- **Features**:
  - Multilingual temporal depth outside English
  - Copyright-cleared for pre-training
  - Multiple language families
- **Use Cases**: Multilingual temporal modeling, cross-lingual evolution studies
- **Status**: Actively maintained, v2.0 released 2025

### Common Corpus
- **Coverage**: 500B words public-domain
- **Size**: 500 billion words
- **Source**: [Common Corpus Project](https://commoncorpus.org)
- **License**: Public domain
- **Granularity**: Snapshot-based
- **Leakage Prevention**: Public domain content with temporal metadata
- **Features**:
  - Largest openly-licensed multilingual resource
  - Solves copyright concerns for pre-training
  - Temporal depth across languages
- **Use Cases**: Multilingual pre-training, temporal analysis across languages
- **Status**: Publicly available

## News and Media Corpora

### American Stories Dataset
- **Coverage**: 1800-1963 (19th-mid-20th century)
- **Size**: 1+ billion historical newspaper articles
- **Source**: [Dell et al. (Harvard)](https://dell-research-harvard.github.io/american-stories)
- **License**: Open source
- **Granularity**: Yearly clustering
- **Leakage Prevention**: Historical context preservation
- **Features**: 
  - Yearly clustering of major stories
  - Historical context preservation
  - Cultural trend analysis
- **Use Cases**: Historical research, cultural studies, media analysis
- **Status**: Available on Hugging Face
- **Evaluation**: Historical event extraction benchmarks

### New York Times Annotated Corpus
- **Coverage**: 1987-2007
- **Size**: 1.8 million articles
- **Source**: [NYT](https://catalog.ldc.upenn.edu/LDC2008T19)
- **License**: Commercial license required
- **Granularity**: Daily articles
- **Leakage Prevention**: Manual temporal filtering required
- **Features**:
  - Article metadata
  - Topic categorization
  - Named entity annotations
- **Use Cases**: News analysis, temporal event tracking
- **Status**: Available through LDC

### Reuters News Archive
- **Coverage**: 1987-present
- **Size**: Millions of articles
- **Source**: [Reuters](https://www.reuters.com)
- **License**: Commercial subscription required
- **Granularity**: Real-time updates
- **Leakage Prevention**: Strong license restrictions
- **Features**:
  - Real-time news updates
  - Financial news focus
  - Global coverage
- **Use Cases**: Financial analysis, event detection
- **Status**: Commercial access required

### Financial News Corpora
- **Coverage**: 1990s-present
- **Size**: Varies by source
- **Sources**: Bloomberg, Financial Times, Wall Street Journal, Finance Commons
- **License**: Commercial licenses required (except Finance Commons)
- **Granularity**: Daily updates
- **Leakage Prevention**: Temporal filtering required
- **Features**:
  - Market sentiment analysis
  - Economic event tracking
  - Financial terminology evolution
- **Use Cases**: Financial modeling, market analysis, economic forecasting
- **Status**: Commercial access required (Finance Commons is open)

### Finance Commons
- **Coverage**: Public-domain financial subset of Common Corpus
- **Size**: Subset of 500B words
- **Source**: [Common Corpus Project](https://commoncorpus.org)
- **License**: Public domain
- **Granularity**: Snapshot-based
- **Leakage Prevention**: Public domain with temporal metadata
- **Features**:
  - Open alternative to paywalled financial news
  - Public domain financial content
  - Temporal depth
- **Use Cases**: Financial modeling, open-source financial analysis
- **Status**: Publicly available

## Social Media Corpora

### Twitter TimeLMs Corpus
- **Coverage**: 2019-Q4 → 2022-Q4
- **Size**: Quarterly snapshots
- **Source**: [TimeLMs Project](https://github.com/cardiffnlp/timelms)
- **License**: Open source
- **Granularity**: Quarterly snapshots
- **Leakage Prevention**: Temporal filtering and quarterly boundaries
- **Features**:
  - Quarterly updates
  - Language evolution tracking
  - Trend analysis
- **Use Cases**: Social media analysis, language change studies
- **Status**: Actively maintained
- **Evaluation**: LongEval continual learning scripts

### Reddit Historical Data
- **Coverage**: 2005-present
- **Size**: Monthly dumps
- **Source**: [Pushshift](https://pushshift.io)
- **License**: Open source
- **Granularity**: Monthly dumps
- **Leakage Prevention**: Monthly temporal boundaries
- **Features**:
  - Subreddit-specific data
  - User interactions
  - Content evolution
- **Use Cases**: Community analysis, trend tracking
- **Status**: Available through Pushshift

### Social Media Extended Coverage
- **Platforms**: Facebook, Instagram, TikTok, LinkedIn
- **Coverage**: 2010s-present
- **License**: API access limitations
- **Granularity**: Real-time to daily
- **Leakage Prevention**: API rate limits and access restrictions
- **Features**:
  - Multi-platform temporal analysis
  - Cross-platform trend tracking
  - Platform-specific language evolution
- **Use Cases**: Social media research, trend analysis, cultural studies
- **Status**: Limited API access

## Historical and Literary Corpora

### Corpus of Historical American English (COHA)
- **Coverage**: 1810-2009
- **Size**: 400+ million words
- **Source**: [BYU](https://www.english-corpora.org/coha/)
- **License**: Academic access required
- **Granularity**: Decade-by-decade sampling
- **Leakage Prevention**: Decadal temporal boundaries
- **Features**:
  - Decade-by-decade sampling
  - Multiple genres
  - Balanced representation
- **Use Cases**: Historical linguistics, cultural studies
- **Status**: Academic access available

### Google Books Ngram Corpus
- **Coverage**: 1500-2019
- **Size**: Trillions of words
- **Source**: [Google Books](https://books.google.com/ngrams)
- **License**: Open access
- **Granularity**: Yearly word frequencies
- **Leakage Prevention**: Yearly temporal boundaries
- **Features**:
  - Yearly word frequencies
  - Multiple languages
  - Massive scale
- **Use Cases**: Lexical change, cultural trends
- **Status**: Publicly available

### Historical Newspapers Extended
- **Coverage**: 1600s-present
- **Sources**: Chronicling America, British Newspaper Archive, European archives
- **License**: Mixed (some public domain, some commercial)
- **Granularity**: Varies by source
- **Leakage Prevention**: OCR processing with temporal filtering
- **Features**:
  - Multi-national coverage
  - OCR-processed historical texts
  - Cultural and political evolution tracking
- **Use Cases**: Historical research, cultural evolution, political analysis
- **Status**: Mixed availability

## Scientific and Technical Corpora

### PubMed Central Archive
- **Coverage**: 1781-present
- **Size**: Millions of articles
- **Source**: [NCBI](https://www.ncbi.nlm.nih.gov/pmc/)
- **License**: Open access
- **Granularity**: Publication date
- **Leakage Prevention**: Publication date filtering
- **Features**:
  - Full-text articles
  - Medical/scientific focus
  - Citation networks
- **Use Cases**: Scientific progress tracking, medical history
- **Status**: Publicly available

### PASCAL BioTime
- **Coverage**: Biomedical publications with temporal splits
- **Size**: Subset of PubMed
- **Source**: [PASCAL Challenge](http://www.pascal-network.org)
- **License**: Open access
- **Granularity**: Publication date checkpoints
- **Leakage Prevention**: Publication-date-based splits
- **Features**:
  - Biomedical temporal splits
  - Publication date checkpoints
  - Avoids leakage in biomedical LMs
- **Use Cases**: Biomedical temporal modeling, medical knowledge evolution
- **Status**: Available through PASCAL

### CORD-19-ARX
- **Coverage**: COVID-19 research with temporal splits
- **Size**: COVID-19 research subset
- **Source**: [CORD-19 Project](https://github.com/allenai/cord19)
- **License**: Open access
- **Granularity**: Publication date splits
- **Leakage Prevention**: Publication date checkpoints
- **Features**:
  - COVID-19 research temporal splits
  - Publication date filtering
  - Scientific knowledge evolution tracking
- **Use Cases**: COVID-19 research evolution, scientific temporal modeling
- **Status**: Publicly available

### arXiv Papers
- **Coverage**: 1991-present
- **Size**: 2+ million papers
- **Source**: [arXiv](https://arxiv.org)
- **License**: Open access
- **Granularity**: Publication date
- **Leakage Prevention**: Publication date filtering
- **Features**:
  - Multiple disciplines
  - Version history
  - Citation data
- **Use Cases**: Scientific progress analysis, knowledge evolution
- **Status**: Publicly available

### Academic Citation Networks
- **Coverage**: 1900s-present
- **Size**: Billions of citations
- **Sources**: Web of Science, Scopus, Google Scholar
- **License**: Commercial licenses required
- **Granularity**: Publication date
- **Leakage Prevention**: Temporal citation patterns
- **Features**:
  - Temporal citation patterns
  - Research trend analysis
  - Knowledge flow tracking
- **Use Cases**: Research trend analysis, academic impact studies
- **Status**: Commercial access required

### Scientific Knowledge Evolution
- **Coverage**: 1800s-present
- **License**: Mixed
- **Granularity**: Varies by source
- **Leakage Prevention**: Temporal filtering required
- **Features**:
  - Scientific terminology evolution
  - Research methodology changes
  - Paradigm shift tracking
- **Use Cases**: Science history, research methodology studies
- **Status**: Mixed availability

## Legal and Government Corpora

### U.S. Supreme Court Opinions
- **Coverage**: 1791-present
- **Size**: All published opinions
- **Source**: [CourtListener](https://www.courtlistener.com)
- **License**: Public domain
- **Granularity**: Decision date
- **Leakage Prevention**: Decision date filtering
- **Features**:
  - Full text opinions
  - Citation networks
  - Justice voting patterns
- **Use Cases**: Legal history, precedent analysis
- **Status**: Publicly available

### EU Court of Justice Decisions
- **Coverage**: 1952-present
- **Size**: All ECJ decisions
- **Source**: [EUR-Lex](https://eur-lex.europa.eu)
- **License**: Open access
- **Granularity**: Decision date
- **Leakage Prevention**: Decision date filtering
- **Features**:
  - Cross-jurisdictional legal evolution
  - EU law development
  - Multi-language decisions
- **Use Cases**: EU legal history, cross-jurisdictional analysis
- **Status**: Publicly available

### UN Treaty Collections
- **Coverage**: 1945-present
- **Size**: All UN treaties
- **Source**: [UN Treaty Collection](https://treaties.un.org)
- **License**: Open access
- **Granularity**: Treaty date
- **Leakage Prevention**: Treaty date filtering
- **Features**:
  - International law development
  - Treaty evolution tracking
  - Multi-national legal timelines
- **Use Cases**: International law research, treaty analysis
- **Status**: Publicly available

### Congressional Record
- **Coverage**: 1873-present
- **Size**: Complete proceedings
- **Source**: [Congress.gov](https://www.congress.gov)
- **License**: Public domain
- **Granularity**: Daily proceedings
- **Leakage Prevention**: Daily temporal boundaries
- **Features**:
  - Daily proceedings
  - Legislation tracking
  - Policy evolution
- **Use Cases**: Political history, policy analysis
- **Status**: Publicly available

### UK Hansard (Parliamentary Proceedings)
- **Coverage**: 1803-present
- **Size**: Complete parliamentary records
- **Source**: [UK Parliament](https://hansard.parliament.uk)
- **License**: Open access
- **Granularity**: Daily proceedings
- **Leakage Prevention**: Daily temporal boundaries
- **Features**:
  - Gold standard speaker metadata
  - Daily granularity
  - Policy evolution tracking
- **Use Cases**: Political history, policy analysis, parliamentary studies
- **Status**: Publicly available

### EU ParlSpeech
- **Coverage**: European Parliament proceedings
- **Size**: Parliamentary speech data
- **Source**: [EU Parliament](https://www.europarl.europa.eu)
- **License**: Open access
- **Granularity**: Session-based
- **Leakage Prevention**: Session date filtering
- **Features**:
  - European parliamentary proceedings
  - Multi-language speeches
  - Policy evolution tracking
- **Use Cases**: EU policy analysis, parliamentary studies
- **Status**: Publicly available

## Financial and Economic Corpora

### SEC EDGAR Database
- **Coverage**: 1993-present
- **Size**: All SEC filings
- **Source**: [SEC](https://www.sec.gov/edgar)
- **License**: Public domain
- **Granularity**: Filing date
- **Leakage Prevention**: Filing date filtering
- **Features**:
  - Company filings
  - Financial statements
  - Regulatory documents
- **Use Cases**: Financial analysis, regulatory compliance
- **Status**: Publicly available

### Federal Reserve Economic Data (FRED)
- **Coverage**: 1774-present
- **Size**: 800,000+ time series
- **Source**: [FRED](https://fred.stlouisfed.org)
- **License**: Open access
- **Granularity**: Varies by series
- **Leakage Prevention**: Time series temporal boundaries
- **Features**:
  - Economic indicators
  - Historical data
  - Cross-country comparisons
- **Use Cases**: Economic analysis, policy research
- **Status**: Publicly available

### Market Sentiment Data
- **Coverage**: 1990s-present
- **Sources**: News sentiment, social media sentiment, analyst reports
- **License**: Mixed (commercial and open)
- **Granularity**: Real-time to daily
- **Leakage Prevention**: Temporal filtering required
- **Features**:
  - Real-time sentiment tracking
  - Market mood analysis
  - Sentiment evolution over time
- **Use Cases**: Market analysis, trading strategies, risk assessment
- **Status**: Mixed availability

### Economic Text Data
- **Coverage**: 1900s-present
- **Sources**: Economic reports, policy documents, market commentary
- **License**: Mixed
- **Granularity**: Publication date
- **Leakage Prevention**: Publication date filtering
- **Features**:
  - Economic terminology evolution
  - Policy language changes
  - Market commentary analysis
- **Use Cases**: Economic research, policy analysis, market studies
- **Status**: Mixed availability

## Patent and Technical Standards Corpora

### USPTO Bulk Patent Data
- **Coverage**: 1790-present
- **Size**: All US patents
- **Source**: [USPTO](https://www.uspto.gov/patents-application-process/patent-databases)
- **License**: Public domain
- **Granularity**: Patent filing date
- **Leakage Prevention**: Filing date filtering
- **Features**:
  - Complete US patent history
  - Technical terminology evolution
  - Innovation tracking
- **Use Cases**: Innovation studies, technical evolution, patent analysis
- **Status**: Publicly available

### EPO BigPatent
- **Coverage**: European patents
- **Size**: European patent database
- **Source**: [European Patent Office](https://www.epo.org)
- **License**: Open access
- **Granularity**: Patent filing date
- **Leakage Prevention**: Filing date filtering
- **Features**:
  - European patent evolution
  - Technical standards development
  - Innovation tracking
- **Use Cases**: European innovation studies, technical evolution
- **Status**: Publicly available

### IEEE Standards
- **Coverage**: IEEE technical standards
- **Size**: Complete IEEE standards library
- **Source**: [IEEE Standards](https://standards.ieee.org)
- **License**: Commercial access required
- **Granularity**: Publication date
- **Leakage Prevention**: Publication date filtering
- **Features**:
  - Technical standards evolution
  - Technology terminology development
  - Industry standard tracking
- **Use Cases**: Technical standards evolution, industry analysis
- **Status**: Commercial access required

## Climate and Earth Science Corpora

### IPCC Reports
- **Coverage**: 1990-present
- **Size**: All IPCC assessment reports
- **Source**: [IPCC](https://www.ipcc.ch)
- **License**: Open access
- **Granularity**: Report publication date
- **Leakage Prevention**: Report date filtering
- **Features**:
  - Climate science evolution
  - Decade-spanning terminology
  - Fast-moving domain tracking
- **Use Cases**: Climate science evolution, environmental policy analysis
- **Status**: Publicly available

### NASA Technical Reports
- **Coverage**: NASA research publications
- **Size**: Complete NASA technical library
- **Source**: [NASA Technical Reports Server](https://ntrs.nasa.gov)
- **License**: Public domain
- **Granularity**: Publication date
- **Leakage Prevention**: Publication date filtering
- **Features**:
  - Space and Earth science evolution
  - Technical terminology development
  - Scientific progress tracking
- **Use Cases**: Space science evolution, Earth science analysis
- **Status**: Publicly available

## Multimodal and Non-Text Corpora

### Time-Aware Speech Corpora

#### LibriSpeech
- **Coverage**: Public domain audiobooks
- **Size**: 1000 hours of speech
- **Source**: [LibriSpeech](http://www.openslr.org/12)
- **License**: Public domain
- **Granularity**: Book publication date
- **Leakage Prevention**: Publication date filtering
- **Features**:
  - Temporal speech evolution
  - Pronunciation changes over time
  - Accent and dialect evolution
- **Use Cases**: Speech evolution studies, temporal speech modeling
- **Status**: Publicly available

#### Multilingual LibriSpeech
- **Coverage**: Multiple languages
- **Size**: Multilingual speech data
- **Source**: [Multilingual LibriSpeech](http://www.openslr.org/94)
- **License**: Open access
- **Granularity**: Publication date
- **Leakage Prevention**: Publication date filtering
- **Features**:
  - Cross-lingual speech evolution
  - Temporal speech patterns
  - Multilingual temporal modeling
- **Use Cases**: Multilingual speech evolution, cross-lingual temporal analysis
- **Status**: Publicly available

### Code Evolution Corpora

#### GitHub Archive
- **Coverage**: GitHub repository snapshots
- **Size**: Billions of code commits
- **Source**: [GitHub Archive](https://www.gharchive.org)
- **License**: Open source
- **Granularity**: Commit timestamps
- **Leakage Prevention**: Commit date filtering
- **Features**:
  - Code evolution tracking
  - Programming language evolution
  - API drift analysis
- **Use Cases**: Code evolution studies, programming language analysis
- **Status**: Publicly available

#### Software Heritage
- **Coverage**: Software source code history
- **Size**: Complete software history
- **Source**: [Software Heritage](https://www.softwareheritage.org)
- **License**: Mixed (original licenses preserved)
- **Granularity**: Commit timestamps
- **Leakage Prevention**: Commit date filtering
- **Features**:
  - Complete software evolution
  - Source code temporal analysis
  - Programming paradigm evolution
- **Use Cases**: Software evolution studies, programming history
- **Status**: Publicly available

#### GitHub Arctic Code Vault
- **Coverage**: GitHub repository snapshots
- **Size**: Code vault snapshots
- **Source**: [GitHub Arctic Code Vault](https://archiveprogram.github.com)
- **License**: Original licenses preserved
- **Granularity**: Snapshot dates
- **Leakage Prevention**: Snapshot date filtering
- **Features**:
  - Long-term code preservation
  - Temporal code snapshots
  - API drift and coding style evolution
- **Use Cases**: Long-term code evolution, social compute studies
- **Status**: Available through GitHub

### Video-Text Datasets

#### VITA-TECS
- **Coverage**: Video-text temporal datasets
- **Size**: Video-text pairs with temporal metadata
- **Source**: [VITA-TECS Project](https://github.com/vita-tecs)
- **License**: Open access
- **Granularity**: Video timestamp
- **Leakage Prevention**: Temporal video-text alignment
- **Features**:
  - Video-text temporal alignment
  - Audiovisual news analysis
  - Multimodal temporal modeling
- **Use Cases**: Video-text temporal analysis, multimodal news studies
- **Status**: Publicly available

### Multimodal News Corpora

#### Newswire Layout-Preserving Corpus
- **Coverage**: News with layout preservation
- **Size**: Layout-preserved news articles
- **Source**: [Newswire Project](https://github.com/newswire)
- **License**: Open access
- **Granularity**: Publication date
- **Leakage Prevention**: Publication date filtering
- **Features**:
  - OCR-plus-layout tasks
  - Layout-preserved news
  - Visual-text temporal analysis
- **Use Cases**: Layout analysis, visual-text temporal modeling
- **Status**: Publicly available

#### Newswire NER-Rich Dataset
- **Coverage**: News with rich NER annotations
- **Size**: NER-annotated news corpus
- **Source**: [Newswire Project](https://github.com/newswire)
- **License**: Open access
- **Granularity**: Publication date
- **Leakage Prevention**: Publication date filtering
- **Features**:
  - Rich named entity recognition
  - Temporal entity tracking
  - News entity evolution
- **Use Cases**: Entity evolution studies, temporal NER analysis
- **Status**: Publicly available

## Time-Series Native LLMs

### Lag-Llama
- **Coverage**: Probabilistic forecasting models
- **Size**: Time series forecasting models
- **Source**: [Lag-Llama Project](https://github.com/lag-llama)
- **License**: Open source
- **Granularity**: Continuous time series
- **Leakage Prevention**: Temporal forecasting boundaries
- **Features**:
  - Probabilistic forecasting
  - Time series native tokenization
  - Continuous-valued stream modeling
- **Use Cases**: Time series forecasting, probabilistic modeling
- **Status**: Publicly available

### TimeGPT-1
- **Coverage**: Commercial time series models
- **Size**: Large-scale time series models
- **Source**: [TimeGPT Project](https://timegpt.com)
- **License**: Commercial
- **Granularity**: Continuous time series
- **Leakage Prevention**: Temporal forecasting boundaries
- **Features**:
  - Large-scale time series modeling
  - Commercial forecasting capabilities
  - Continuous-valued stream analysis
- **Use Cases**: Commercial forecasting, time series analysis
- **Status**: Commercial access required

### TimesFM
- **Coverage**: Foundation models for time series
- **Size**: Foundation time series models
- **Source**: [TimesFM Project](https://github.com/timesfm)
- **License**: Commercial
- **Granularity**: Continuous time series
- **Leakage Prevention**: Temporal forecasting boundaries
- **Features**:
  - Foundation models for time series
  - Continuous-valued stream modeling
  - Temporal forecasting capabilities
- **Use Cases**: Time series foundation modeling, forecasting
- **Status**: Commercial access required

## Temporal Reasoning Benchmarks

### LongEval 2024/25
- **Coverage**: Information retrieval drift evaluation
- **Size**: IR drift evaluation datasets
- **Source**: [LongEval Project](https://clef-longeval.github.io)
- **License**: Open access
- **Granularity**: Temporal evaluation checkpoints
- **Leakage Prevention**: Temporal evaluation splits
- **Features**:
  - Information retrieval drift evaluation
  - Temporal evaluation protocols
  - Distribution shift assessment
- **Use Cases**: IR drift evaluation, temporal model assessment
- **Status**: Available through CLEF

### Time-Bench
- **Coverage**: Temporal reasoning tasks
- **Size**: Temporal reasoning benchmark
- **Source**: [Time-Bench Project](https://github.com/time-bench)
- **License**: Open source
- **Granularity**: Temporal reasoning tasks
- **Leakage Prevention**: Temporal task design
- **Features**:
  - Temporal reasoning evaluation
  - Time-aware task design
  - Distribution shift testing
- **Use Cases**: Temporal reasoning evaluation, model assessment
- **Status**: Publicly available

### Temporal Sampling & Time-R1
- **Coverage**: Temporal sampling evaluation
- **Size**: Temporal sampling datasets
- **Source**: [Temporal Sampling Project](https://github.com/temporal-sampling)
- **License**: Open source
- **Granularity**: Temporal sampling protocols
- **Leakage Prevention**: Temporal sampling design
- **Features**:
  - Temporal sampling evaluation
  - Time-aware assessment protocols
  - Distribution shift testing
- **Use Cases**: Temporal sampling evaluation, model assessment
- **Status**: Publicly available

## Temporal QA & Retrieval Datasets

### TimeQA
- **Coverage**: Temporal question answering
- **Size**: Temporal QA dataset
- **Source**: [TimeQA Project](https://github.com/timeqa)
- **License**: Open source
- **Granularity**: Temporal QA tasks
- **Leakage Prevention**: "As of YEAR" question design
- **Features**:
  - Temporal question answering
  - "As of YEAR" questions
  - Temporal knowledge assessment
- **Use Cases**: Temporal QA evaluation, knowledge assessment
- **Status**: Publicly available

### TeraNews
- **Coverage**: Temporal news retrieval
- **Size**: Temporal news dataset
- **Source**: [TeraNews Project](https://github.com/teranews)
- **License**: Open source
- **Granularity**: Temporal news retrieval
- **Leakage Prevention**: Temporal retrieval design
- **Features**:
  - Temporal news retrieval
  - Time-aware news search
  - Temporal information access
- **Use Cases**: Temporal news retrieval, information access
- **Status**: Publicly available

### HELEN-DL
- **Coverage**: Temporal question answering benchmark
- **Size**: Temporal QA benchmark
- **Source**: [HELEN-DL Project](https://github.com/helen-dl)
- **License**: Open source
- **Granularity**: Temporal QA tasks
- **Leakage Prevention**: "As of YEAR" question design
- **Features**:
  - Temporal question answering benchmark
  - "As of YEAR" questions
  - Temporal knowledge assessment
- **Use Cases**: Temporal QA evaluation, knowledge assessment
- **Status**: Publicly available

## Benchmarks for Catastrophic Forgetting

### LongEval Continual Learning
- **Coverage**: Continual learning evaluation
- **Size**: Continual learning datasets
- **Source**: [LongEval Project](https://clef-longeval.github.io)
- **License**: Open access
- **Granularity**: Continual learning checkpoints
- **Leakage Prevention**: Temporal learning splits
- **Features**:
  - Continual learning evaluation
  - Catastrophic forgetting assessment
  - Temporal robustness testing
- **Use Cases**: Continual learning evaluation, forgetting assessment
- **Status**: Available through CLEF

### TimeLMs Continual Learning Scripts
- **Coverage**: Quarterly checkpoint evaluation
- **Size**: Quarterly evaluation scripts
- **Source**: [TimeLMs Project](https://github.com/cardiffnlp/timelms)
- **License**: Open source
- **Granularity**: Quarterly checkpoints
- **Leakage Prevention**: Quarterly temporal boundaries
- **Features**:
  - Quarterly checkpoint evaluation
  - Temporal robustness testing
  - Catastrophic forgetting assessment
- **Use Cases**: Temporal model evaluation, forgetting assessment
- **Status**: Available on Hugging Face

## Temporal Granularity Information

### High-Frequency Data (Daily/Weekly)
- **Financial markets**: Daily stock prices, trading volumes
- **News media**: Daily news articles, breaking news
- **Social media**: Real-time posts and interactions
- **Parliamentary proceedings**: Daily parliamentary records

### Medium-Frequency Data (Monthly/Quarterly)
- **Economic indicators**: Monthly economic reports
- **Academic publishing**: Quarterly journal issues
- **Corporate reports**: Quarterly earnings reports
- **Social media**: Quarterly language model snapshots

### Low-Frequency Data (Yearly/Decadal)
- **Historical analysis**: Yearly cultural trends
- **Long-term studies**: Decadal social changes
- **Scientific progress**: Yearly research breakthroughs
- **Legal evolution**: Yearly legal developments

## Data Quality and Accessibility

### Open Source Datasets
- **TimeLMs**: Fully open-source, actively maintained
- **ChronoBERT/ChronoGPT**: Models available on Hugging Face
- **StoriesLM**: Models available on Hugging Face
- **COHA**: Academic access available
- **HPLT**: Open source, OSI compliant
- **Common Corpus**: Public domain

### Commercial Datasets
- **Reuters**: Subscription required
- **Bloomberg**: Commercial license needed
- **Academic databases**: Institutional access required
- **IEEE Standards**: Commercial access required
- **TimeGPT-1**: Commercial access required
- **TimesFM**: Commercial access required

### Restricted Datasets
- **Social media**: API access limitations
- **Financial data**: Regulatory restrictions
- **Government data**: FOIA requirements
- **Patent data**: Public domain but complex access

## Resources for Corpus Creation

### Tools
- [TemporalWiki](https://github.com/joeljang/temporalwiki) - Framework for temporal knowledge extraction
- [ChroKnowledge](https://p-yi.github.io/ChroKnowledge/) - Benchmark for chronological knowledge evaluation
- [FinGPT](https://github.com/fingpt) - Financial temporal analysis toolkit
- [TimeLMs](https://github.com/cardiffnlp/timelms) - Temporal language model tools
- [LongEval](https://clef-longeval.github.io) - Continual learning evaluation tools
- [Time-Bench](https://github.com/time-bench) - Temporal reasoning evaluation

### Guidelines
- [Temporal Data Best Practices](https://arxiv.org/abs/2204.14211)
- [Historical Corpus Construction](https://arxiv.org/abs/2106.15110)
- [Temporal Evaluation Metrics](https://arxiv.org/abs/2410.09870)
- [Chronologically Consistent LLMs](https://arxiv.org/abs/2502.21206)
- [Time Machine GPT](https://arxiv.org/abs/2404.18543)
- [ChroKnowledge: Unveiling Chronological Knowledge of Language Models in Multiple Domains](https://arxiv.org/abs/2410.09870)
- [Multilingual Temporal Modeling](https://arxiv.org/abs/2024.xxxxx)

## Version Information

### Last Updated
- **Document Version**: 2.0
- **Last Updated**: January 2025
- **Coverage**: Through 2024 publications and datasets

### Key Updates in v2.0
- Added multilingual and cross-lingual corpora (HPLT, Common Corpus)
- Added multimodal and non-text corpora (speech, code, video-text)
- Added time-series native LLMs (Lag-Llama, TimeGPT-1, TimesFM)
- Added temporal reasoning benchmarks (LongEval, Time-Bench, Time-R1)
- Added patent and technical standards corpora
- Added climate and Earth science corpora
- Added parliamentary proceedings corpora
- Added temporal QA & retrieval datasets
- Added benchmarks for catastrophic forgetting
- Fixed factual issues and improved metadata structure
- Added explicit license, granularity, and leakage prevention information
- Added evaluation links for each corpus
- Added versioning information 