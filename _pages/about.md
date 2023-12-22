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
I am a full-time research assistant at the Center for Public Health Genomics in University of Virginia School of Medicine
advised by [Prof. Chongzhi Zang](https://zanglab.github.io/index.htm).

Previously, I received my Master's degree in Computer Science from Johns Hopkins University and 
Bachelor's degree in Computer Science from Wenzhou-Kean University. I did my master thesis with Prof. Kimia Ghobadi at Johns Hopkins on multi-agent simulation.
I was fortunate to work with Prof. Aloysius Wong's group where I first stepped into the field of bioinformatics. In addition, I developed a 
model for RNA-ligand affinity prediction in Prof. Yanjun Li's group at UFL and later participated in single-cell foundation model development 
in Prof. Xiaojie Qiu's Lab at Stanford.

My research interests lie in bioinformatics, computational biology, deep learning, and AI for science.
I also have software engineering experiences with Java, Python, Go, React.js, MySQL.

# 📖 Educations
- *2022.08 - 2023.12*, Master of Science in Engineering, Computer Science. Johns Hopkins University. *Baltimore, MD* 
- *2018.08 - 2022.05*, Bachelor of Science, Computer Science. Wenzhou-Kean University. *Wenzhou, China*

# 📰 News
[//]: # (- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.)

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

[Website](https://www.hnoxpred.com/)  [Code](https://github.com/JasonJiangs/HNOX_Pred)
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

# Research Experience
- *2023.06 - Present*, Lab Specialist, [Chongzhi Zang Lab](https://zanglab.github.io/index.htm), University of Virginia School of Medicine, Charlottesville, VA.
- *2023.08 - 2023.12*, Research Assistant, [Xiaojie Qiu Lab](https://www.devo-evo.com/), Stanford University, Remote.
- *2023.06 - 2023.12*, Research Assistant, [Yanjun Li Lab](https://yanjun-li.com/index.html), University of Florida College of Pharmacy, Remote.
- *2022.09 - 2023.09*, Research Assistant, [Kimia Ghobadi Lab](https://systems.jhu.edu/kimia/), Johns Hopkins Withing School of Engineering, Baltimore, MD.
- *2021.08 - 2022.06*, Research Assistant, [Aloysius Wong Lab](https://wku.edu.cn/faculty/aloysius-wong/), Wenzhou-Kean University.

# Industry
- *2022.06 - 2022.08*, Software Engineer Intern, [Alibaba Cloud - PolarDB](https://www.alibabacloud.com/product/polardb), Hangzhou, China.
- *2021.09 - 2022.03*, Applied Research Intern, [Institute of Automation](https://people.ucas.edu.cn/~zhenshen?language=en), Chinese Academy of Sciences, Beijing, China.


# 🧑‍💻 Software

[//]: # (## Deep Learning Model)

[//]: # (- [scTab]&#40;&#41;: A)

[//]: # (- [AIDD]&#40;&#41;: )

## Research Pipeline & Model

[//]: # (- [Nano-plastics ML]&#40;https://github.com/Haoxin01/Nanoplastics-ML&#41;: This work applies machine learning to forecast types and concentrations of nanoplastics in the environment.)
- [Koudou](https://github.com/caranha/Koudou): 
  This is an agent-based model that simulates the infectious diseases.

[//]: # (- [RNA-seq & ChIP-seq Joint Analysis Pipeline]&#40;https://github.com/JasonJiangs/RNAseq-ChIPseq-Joint-Pipeline&#41;: )

[//]: # (  This pipeline integrates RNA-seq and ChIP-seq tools for analyzing transcriptional regulation, configured easily through YAML files and command-line arguments.)

## Web server
- [HNOXPred](https://github.com/JasonJiangs/HNOX_Pred) (**Pred**iction of **H**eme-**N**itric oxide/**OX**ygen domains):
  This web server predicts gas-sensing H-NOX proteins from amino acid sequences, returning H-NOX centers and scores scaled from 0 to 1 based on comparisons to the HNOXPred database.

[//]: # (- [Koudou Simulator Analyser]&#40;https://github.com/caranha/Koudou/tree/ALIFE_2023/src/dashapp&#41;:)

[//]: # (  This web tool provides statistical, geographical, and visualization analysis of infectious disease simulations for the Koudou Simulator, allowing comparative analysis.)

# 🌎 Miscellaneous
Soccer (Visca Barça~), Gym, Table tennis, Piano, Traveling, etc.

<body>
  <a href="https://clustrmaps.com/site/1bt6x"  title="Visit tracker" >
    <img src="//www.clustrmaps.com/map_v2.png?d=aGpjzbKbHZT-5oLEhHvcK0igPnT7IvQmYxySQX6oPb4&cl=ffffff" />
  </a>
</body>