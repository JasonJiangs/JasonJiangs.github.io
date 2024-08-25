---
permalink: /
title: "Shiyu Jiang"
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

# 🗨 About Me
I am currently a research intern at the [Representation Learning Lab](https://github.com/westlake-repl) 
at the Westlake University working with Prof. Fajie Yuan.

Previously, I received my Master's degree in Computer Science from Johns Hopkins University and 
Bachelor's degree in Computer Science from Wenzhou-Kean University. 
I did my master thesis advised by Prof. Kimia Ghobadi at [Johns Hopkins University](https://systems.jhu.edu/kimia/) on multi-agent simulation.
I was fortunate to work with Prof. Aloysius Wong's group at [Wenzhou-Kean University](https://csmt.wku.edu.cn/en/node/1777) 
where I first stepped into the field of bioinformatics. 
In addition, I developed a deep learning model for RNA-ligand interaction prediction with Prof. Yanjun Li at [University of Florida](https://yanjun-li.com/index.html) 
and later participated in developing a single-cell foundation model in Prof. Xiaojie Qiu's Lab at [Stanford University](https://www.devo-evo.com/).

I mainly work on the intersection of machine learning and biology in a broad scope. I am interested in foundation 
models and LLMs for science including single-cell, RNA, and protein, and how to use them to discover and 
interpret the biological mechanism.

Research Interests:
- Genomics
- Deep learning for Cancer Biology and Chemical Biology
- AI for Drug Discovery

[//]: # (- Artificial Life)

# 📖 Educations

[//]: # (- *2024.08 - Present*, Doctor of Philosophy, Computational Biology.)
- *2022 - 2024*, Master of Science in Engineering, Computer Science. Johns Hopkins University. *Baltimore, MD* 
- *2018 - 2022*, Bachelor of Science, Computer Science. Wenzhou-Kean University. *Wenzhou, China*

# 📰 News

[//]: # (- *2024.08*: )
[//]: # (- *2024.06*: The follow-up work of building an emotion model for [Koudou]&#40;https://github.com/caranha/Koudou&#41; has been accepted by ALIFE 2024. )
[//]: # (- *2024.03*: [ContraBind]&#40;&#41;, a contrastive learning based model for RNA-small molecules binding affinity prediction has been published as a preprint.)
[//]: # (- *2024.03*: [REFEREE]&#40;&#41;, a federated learning based single-cell foundation model has been published as a preprint.)
[//]: # (- *2024.03*: SICER2, a redesigned ChIP-seq broad peak calling tool, has been updated &#40;check the [Documentation]&#40;https://zanglab.github.io/SICER2/&#41;&#41;.)
[//]: # (- *2023.07*: The work to build based on a multi-agent model for pandemic simulation, [Koudou]&#40;https://github.com/caranha/Koudou&#41;, has been accepted by ALIFE 2023.)

# 📝 Publications
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ALIFE 2023</div><img src='images/covid_sim.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[Simulating Disease Spread During Disaster Scenarios](https://direct.mit.edu/isal/proceedings/isal/35/123/116938)
**Shiyu Jiang**, Heejoong Kim, Fabio Henrique Tanaka, Claus Aranha, Anna Bogdanova, Kimia Ghobadi, Anton Dahbura. *The International Conference on Artificial Life*, 2023.
[Code](https://github.com/caranha/Koudou/tree/ALIFE_2023)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Bioinformatics</div><img src='images/bioinformatics2022.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[HNOXPred: a web tool for the prediction of gas-sensing H-NOX proteins from amino acid sequence](https://academic.oup.com/bioinformatics/article/38/19/4643/6673135)
**Shiyu Jiang**, Hemn Barzan Abdalla, Chuyun Bi, Yi Zhu, Xuechen Tian, Yixin Yang, Aloysius Wong. *Bioinformatics*, 2022
[Website](https://www.hnoxpred.com/) | [Code](https://github.com/JasonJiangs/HNOX_Pred)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IJCNN 2021</div><img src='images/ijcnn.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[Deblur-yolo: Real-time object detection with efficient blind motion deblurring](https://ieeexplore.ieee.org/abstract/document/9534352)

Shen Zheng, Yuxiong Wu, **Shiyu Jiang**, Changjie Lu, Gaurav Gupta. *International Joint Conference on Neural Networks*, 2021

</div>
</div>

[comment]: <> (# 🎖 Honors and Awards)

[comment]: <> (- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. )

[comment]: <> (- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. )

# 🧑‍💻 Professional Experience
- *2024.08 - Present*, Research Intern, [Representation Learning Lab](https://github.com/westlake-repl), Westlake University, *Hangzhou, China*.
- *2024.01 - 2024.07*, Lab Specialist, [Chongzhi Zang Lab](https://zanglab.github.io/index.htm), University of Virginia School of Medicine, *Charlottesville, VA*.
- *2022.06 - 2022.08*, Software Engineer Intern, [Alibaba Cloud - PolarDB](https://www.alibabacloud.com/product/polardb), *Hangzhou, China*.
- *2021.09 - 2022.03*, Applied Research Intern, [Institute of Automation](https://people.ucas.edu.cn/~zhenshen?language=en), Chinese Academy of Sciences, *Beijing, China*.


# 🔨 Tools
## Model
- [Koudou](https://github.com/caranha/Koudou): 
  an agent-based model that simulates the infectious disease spread under college town scenario.

[//]: # (- [scFFM]&#40;https://github.com/OmicsML/scTab&#41;:)

[//]: # (  a federated foundation model for single-cell that enables in-silico gene regulatory inference.)

[//]: # (- [SmartBind]&#40;https://github.com/AIDD-LiLab/RL-CLIP&#41;:)

[//]: # (  a sequence-based DL model for RNA-small molecule binding prediction with efficient virtual screening performance.)

## Web server
- [HNOXPred](https://github.com/JasonJiangs/HNOX_Pred) (**Pred**iction of **H**eme-**N**itric oxide/**OX**ygen domains):
  a web server that predicts gas-sensing H-NOX proteins from amino acid sequences.

## Python Package
- [SICER 2.0](https://zanglab.github.io/SICER2/) (**S**patial-clustering **I**dentification of **C**hIP-**E**nriched **R**egions):
  a ChIP-Seq broad peak calling data analysis method.

# 🌎 Miscellaneous
Soccer (Visca Barça), Gym, Table tennis, Piano, Travel, etc.

<body>
  <a href="https://clustrmaps.com/site/1bt6x"  title="Visit tracker" >
    <img src="//www.clustrmaps.com/map_v2.png?d=aGpjzbKbHZT-5oLEhHvcK0igPnT7IvQmYxySQX6oPb4&cl=ffffff" />
  </a>
</body>