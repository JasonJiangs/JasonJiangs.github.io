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
I am currently working as a visiting researcher at the Westlake University working with [Prof. Fajie Yuan](https://en.westlake.edu.cn/faculty/fajie-yuan.html) and [Dr. Zitong Jerry Wang](https://cellethology.github.io/).

Previously, I received my Master's degree in Computer Science from Johns Hopkins University and 
Bachelor's degree in Computer Science from Wenzhou-Kean University. 
I did my master thesis advised by [Prof. Kimia Ghobadi](https://systems.jhu.edu/kimia/) at Johns Hopkins University on multi-agent simulation.
I was fortunate to work with [Prof. Aloysius Wong's Group](https://csmt.wku.edu.cn/en/node/1777) at Wenzhou-Kean University during my undergraduate
where I first stepped into the field of bioinformatics. After graduation, I worked as a lab specialist at [Prof. Chongzhi Zang's Lab](https://zanglab.github.io/index.htm) at 
the University of Virginia Medical School exploring computational genomics.

In addition, I developed a deep learning model for RNA-ligand interaction prediction with [Prof. Yanjun Li](https://yanjun-li.com/index.html) at University of Florida 
and later participated in developing a single-cell foundation model in [Prof. Xiaojie Qiu's Lab](https://www.devo-evo.com/) at Stanford University. 
I am also working with [Prof. Han Xiao's Group](https://xiao.rice.edu/) at Rice University Chemistry for developing a robust platform
for machine learning guided protein evolution.

[//]: # (Previously, I was working with Prof. Chongzhi Zang &#40;UVa&#41;, Prof. Xiaojie Qiu &#40;Stanford&#41;, Prof. Yanjun Li &#40;UFL&#41;, )

[//]: # (Prof. Han Xiao &#40;Rice&#41;, Dr. Kevin K. Yang &#40;MSR&#41;, Prof. Kimia Ghobadi &#40;JHU&#41;, Prof. Claus Aranha &#40;Tsukuba&#41;, )

[//]: # (Prof. Fajie Yuan &#40;Westlake&#41;, Dr. Jerry Wang &#40;Westlake&#41;, and Prof. Aloysius Wong &#40;WKU&#41;.)

I mainly work on the intersection of machine learning and biology in a broad scope. I am interested in foundation 
models and LLMs for life sciences around the central dogma and how to use them to interpret and 
discover the biological mechanism.

Research Interests:
- Computational genomics
- Deep learning for cancer biology and chemical biology
- AI for drug discovery

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
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">bioRxiv</div><img src='images/qa.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[Decoding the Molecular Language of Proteins with Evola](https://www.biorxiv.org/content/10.1101/2025.01.05.630192v1)
Xibin Zhou †, Chenchen Han †, Yingqi Zhang ‡, Jin Su ‡, Kai Zhuang ‡, **Shiyu Jiang** ‡, Zichen Yuan, Wei Zheng, Fengyuan Dai, Yuyang Zhou, Yuyang Tao, Dan Wu, Fajie Yuan. *bioRxiv*, 2025.
[Demo Website](http://www.chat-protein.com/)
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">bioRxiv</div><img src='images/tabula.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[Toward a privacy-preserving predictive foundation model of single-cell transcriptomics with federated learning and tabular modeling](https://www.biorxiv.org/content/10.1101/2025.01.06.631427v1)
Jiayuan Ding †, Jianhui Lin †, **Shiyu Jiang** †, Yixin Wang, Ziyang Mao, Zhaoyu Fang, Jiliang Tang, Min Li, Xiaojie Qiu. *bioRxiv*, 2025.
[Package](https://github.com/aristoteleo/tabula)
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">bioRxiv</div><img src='images/protrek.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[ProTrek: Navigating the Protein Universe through Tri-Modal Contrastive Learning](https://www.biorxiv.org/content/10.1101/2024.05.30.596740v2.abstract)
Jin Su, Xibin Zhou, Xuting Zhang, Fajie Yuan (To be updated). *bioRxiv*, 2024.
[Demo Website](http://search-protrek.com/)
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">bioRxiv</div><img src='images/saprothub.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[SaprotHub: Making Protein Modeling Accessible to All Biologists](https://www.biorxiv.org/content/10.1101/2024.05.24.595648v5.abstract)
Jin Su, Zhikai Li, Chenchen Han, Yuyang Zhou, Yan He, Junjie Shan, Xibin Zhou, Xing Chang, **Shiyu Jiang**, Dacheng Ma, The OPMC, Martin Steinegger, Sergey Ovchinnikov, Fajie Yuan. *bioRxiv*, 2024.
[Platform](https://github.com/westlake-repl/SaprotHub?tab=readme-ov-file)
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACS Nano</div><img src='images/acsnano.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[Integrating Metal–Phenolic Networks-Mediated Separation and Machine Learning-Aided Surface-Enhanced Raman Spectroscopy for Accurate Nanoplastics Quantification and Classification](https://pubs.acs.org/doi/abs/10.1021/acsnano.4c08316)
Haoxin Ye, **Shiyu Jiang**, Yan Yan, Bin Zhao, Edward R Grant, David D Kitts, Rickey Y Yada, Anubhav Pratap-Singh, Alberto Baldelli, Tianxi Yang. *ACS Nano*, 2024.
[Featured on Cover](https://pubs.acs.org/cms/10.1021/ancac3.2024.18.issue-38/asset/ancac3.2024.18.issue-38.xlargecover-4.jpg)
</div>
</div>


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
- *2024.08 - Present*, Visiting Researcher, [Representation Learning Lab](https://github.com/westlake-repl) & [Cell Ethology Lab](https://cellethology.github.io/), Westlake University, *Hangzhou, China*.
- *2024.01 - 2024.07*, Lab Specialist, [Chongzhi Zang Lab](https://zanglab.github.io/index.htm), University of Virginia School of Medicine, *Charlottesville, VA*.
- *2022.06 - 2022.08*, Software Engineer Intern, [Alibaba Cloud - PolarDB](https://www.alibabacloud.com/product/polardb), *Hangzhou, China*.
- *2021.09 - 2022.03*, Applied Research Intern, [Institute of Automation](https://people.ucas.edu.cn/~zhenshen?language=en), Chinese Academy of Sciences, *Beijing, China*.


# 🔨 Tools
## Model
- [Koudou](https://github.com/caranha/Koudou): 
  an agent-based model that simulates the infectious disease spread under college town scenario.

[//]: # (- [ProTrek]&#40;http://search-protrek.com/&#41;:)
  
[//]: # (- [Tabula]&#40;&#41;:)

[//]: # (  a privacy-protected foundation model for single-cell.)

[//]: # (- [SmartBind]&#40;&#41;:)
  

## Web server
- [HNOXPred](https://github.com/JasonJiangs/HNOX_Pred) (**Pred**iction of **H**eme-**N**itric oxide/**OX**ygen domains):
  a web server that predicts gas-sensing H-NOX proteins from amino acid sequences.

## Python Package
- [SICER 2.0](https://zanglab.github.io/SICER2/) (**S**patial-clustering **I**dentification of **C**hIP-**E**nriched **R**egions):
  a ChIP-Seq broad peak calling data analysis method.

# 🌎 Miscellaneous
Outside of work, you’ll often find me at the gym, playing soccer, road cycling, or traveling to new destinations. I also enjoy playing table tennis and the piano occasionally.


<body>
  <a href="https://clustrmaps.com/site/1bt6x"  title="Visit tracker" >
    <img src="//www.clustrmaps.com/map_v2.png?d=aGpjzbKbHZT-5oLEhHvcK0igPnT7IvQmYxySQX6oPb4&cl=ffffff" />
  </a>
</body>