# Point-in-Time Large Language Models (PITLLM)

A resource that summarizes and connects research on Point-in-Time (chronologically consistent) Large Language Models: models trained only on text available up to a fixed cut-off date, so that sequences of them can be used for backtesting and historical analysis without look-ahead bias.

**Site:** https://pitllm.microprediction.org/

## What is on the site

- [Home](https://pitllm.microprediction.org/) - the idea, the released model sequences, research threads, and a verified bibliography
- [Models](https://pitllm.microprediction.org/models.html) - ChronoBERT/ChronoGPT, Scaling PiT LMs, Time Machine GPT, TimeLMs, StoriesLM, HistBERT, with a coverage chart
- [Corpora](https://pitllm.microprediction.org/corpora.html) - dated text sources by domain, with licensing and temporal granularity
- [Key ideas](https://pitllm.microprediction.org/ideas.html) - one note per paper on what is actually new
- [Essay](https://pitllm.microprediction.org/essay.html) - point-in-time LLMs beyond finance
- [Literature map](https://pitllm.microprediction.org/map.html) and [Timeline](https://pitllm.microprediction.org/timeline.html)
- [Demos](https://pitllm.microprediction.org/demos.html) - notebooks that load a checkpoint and query it

## Repository layout

- `docs/` - the static site (plain HTML and CSS, D3 for the map and timeline), deployed by `.github/workflows/pages.yml`
- `ESSAY.md`, `PIT-CORPUSES.md`, `CORPUS-GRANULARITY.md` - source documents rendered on the site
- `SMALL-BUDGET-PLAN.md`, `SMALL-BUDGET-CORPUS-PLAN.md`, `SMALL-BUDGET-CORPUS-SUBNET-PLAN.md` - funding notes, not rendered on the site
- `LLM-PROJECT-LISTING.md` - short list of model sequences and tools
- `projects/` - summaries and PDFs of individual papers
- `ChronoGPT.ipynb` - Colab notebook for sampling from ChronoGPT checkpoints

## Key model sequences

- [ChronoBERT / ChronoGPT](https://arxiv.org/abs/2502.21206) - 26 yearly checkpoints, 1999-2024 ([Hugging Face](https://huggingface.co/collections/manelalab/chronobert-67c1ca6c2382e03aaec446f8))
- [Scaling Point-in-Time Language Models](https://arxiv.org/abs/2607.11889) - monthly checkpoints, 2013-2024, up to 4B parameters
- [Time Machine GPT](https://arxiv.org/abs/2404.18543) - 12 yearly GPT-2 models, 2011-2022 ([Hugging Face](https://huggingface.co/Ti-Ma))
- [TimeLMs](https://github.com/cardiffnlp/timelms) - quarterly RoBERTa checkpoints on Twitter, 2019-2022
- [StoriesLM](https://huggingface.co/StoriesLM) - 64 yearly models, 1900-1963
- [HistBERT](https://github.com/wendyqiu/diachronicBert) - decade-wise BERT on COHA

## Contributing

Open an issue or pull request with a model sequence, corpus, or paper that is missing. References on the site are verified against the arXiv API or Crossref before they are added.
