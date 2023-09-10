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
Hello, my name is Shiyu, a master student majoring in computer science at Whiting School of Engineering, Johns Hopkins University 
advised by [Prof.Kimia Ghobadi](https://systems.jhu.edu/kimia/) and [Prof.Claus Aranha](http://conclave.cs.tsukuba.ac.jp/). 
I'm current working as a part-time research assistant at [Prof.Chongzhi Zang's Lab](https://zanglab.github.io/index.htm) on computational biology.

Previously I received my Bachelor's degree in Computer Science from Wenzhou-Kean University. 
During my undergrad, I was fortunate to work with [Prof.Aloysius Wong](https://wku.edu.cn/faculty/aloysius-wong/).

My research interests lie in bioinformatics, computational biology, deep learning, and AI for science.
I also have experiences in software engineering with Java, Python, Go, and React.js.

# 📖 Educations
- *2022.08 - 2023.12*, Master of Science in Engineering, Computer Science. Whiting School of Engineering, Johns Hopkins University. *Baltimore, MD* 
- *2018.08 - 2022.05*, Bachelor of Science, Computer Science. College of Science and Technology, Wenzhou-Kean University. *Wenzhou, China*

# 📰 News

[//]: # (- *2023.12*: The Work "scTab" at Dr.Qiu's Lab has been accepted by RECOMBE 2024. )

# 💻 Experiences
- *2023.08 - Present*, Research Assistant (Remote), [Qiu Lab](https://www.devo-evo.com/), Stanford University.
  - Single-cell pretrained model.
- *2023.06 - Present*, Research Assistant (Remote), [Li Lab](https://yanjun-li.com/index.html), University of Florida College of Pharmacy.
  - RNA-small molecule interaction.
- *2023.01 - Present*, Research Assistant, [Chongzhi Zang Lab](https://zanglab.github.io/index.htm), University of Virginia School of Medicine, Charlottesville, VA.
  - Computational genomics.
  - ChIP-seq broad peak calling tool redesign.
- *2022.09 - 2023.07*, Research Assistant, [Kimia Ghobadi Lab](https://systems.jhu.edu/kimia/), Johns Hopkins Withing School of Engineering, Baltimore, MD.
  - Multi-agent simulation, affective model, visualization, and network analysis.
  - Master's thesis: Analyzing Epidemic Spread with Agent-based Simulation Model and Network Analysis.
- *2022.06 - 2022.08*, Software Engineer Intern, [Alibaba Cloud - PolarDB](https://www.alibabacloud.com/product/polardb), Hangzhou, China.
  - Technology Used: Java, MySQL, JDBC, ShardingSphere-Proxy, ZooKeeper, JUnit, Mockito.
- *2021.09 - 2022.08*, Deep Learning Research Intern, [Institute of Automation](https://people.ucas.edu.cn/~zhenshen?language=en), Chinese Academy of Sciences, Beijing, China.
  - Deep Learning application in high-frequency trading.
- *2021.08 - 2022.07*, Research Assistant, [Wenzhou Municipal Key Lab for Applied Biomedical Informatics](https://wku.edu.cn/faculty/aloysius-wong/), Wenzhou, China.
  - Developed a user-friendly web server HNOXPred, as a tool for the prediction of gas-sensing H-NOX proteins from amino acid sequence input.


# 📝 Publications

[//]: # (<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ChemRxiv</div><img src='images/nanoplasticsML.png' alt="sym" width="100%"></div></div>)

[//]: # ()
[//]: # (<div class='paper-box-text' markdown="1">)

[//]: # ()
[//]: # ([Specific Detection and High-Precision Quantification of Nanoscale Plastics Enabled by Surface Enhanced Raman Spectroscopy Coupled with Machine Learning]&#40;&#41;)

[//]: # ()
[//]: # (Haoxin Ye, **Shiyu Jiang**, . *ChemRxiv*, 2023.)

[//]: # ()
[//]: # (- This work aims to ...)

[//]: # ()
[//]: # (</div>)

[//]: # ()
[//]: # (</div>)


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ALIFE 2023</div><img src='images/covid_sim.png' alt="sym" width="100%"></div></div>

<div class='paper-box-text' markdown="1">

[Simulating Disease Spread During Disaster Scenarios]()

**Shiyu Jiang**, Heejoong Kim, Fabio Henrique Tanaka, Claus Aranha, Anna Bogdanova, Kimia Ghobadi, Anton Dahbura. *The International Conference on Artificial Life*, 2023.

[Code](https://github.com/caranha/Koudou/tree/ALIFE_2023) [Talk]()

- This research aims to create a comprehensive Agent-Based Model (ABM) to simulate daily agent schedules and movements across Johns Hopkins and University of Tsukuba campuses. The model will compare scenarios related to COVID-19 spread and assess the impact of large-scale events, like earthquakes, on masking policies and disease transmission dynamics.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Bioinformatics</div><img src='images/bioinformatics2022.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[HNOXPred: a web tool for the prediction of gas-sensing H-NOX proteins from amino acid sequence](https://academic.oup.com/bioinformatics/article/38/19/4643/6673135)

**Shiyu Jiang**, Hemn Barzan Abdalla, Chuyun Bi, Yi Zhu, Xuechen Tian, Yixin Yang, Aloysius Wong. *Bioinformatics*, 2022

[Website](https://www.hnoxpred.com/)  [Code](https://github.com/JasonJiangs/HNOX_Pred)

- H-NOX proteins are gas-sensing hemoproteins found in diverse organisms ranging from bacteria to eukaryotes. HNOXPred is a webserver for the prediction of gas-sensing heme-nitric oxide/oxygen (H-NOX) proteins from amino acid sequence.
- The tool is developed by Python scripts, Flask framework and MySQL DB.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IJCNN 2021</div><img src='images/ijcnn.png' alt="sym" width="100%"></div></div>

<div class='paper-box-text' markdown="1">

[Deblur-yolo: Real-time object detection with efficient blind motion deblurring](https://ieeexplore.ieee.org/abstract/document/9534352)

Shen Zheng, Yuxiong Wu, **Shiyu Jiang**, Changjie Lu, Gaurav Gupta. *International Joint Conference on Neural Networks*, 2021

- In this work, we propose Deblur-YOLO, an efficient, YOLO-based and detection-driven approach robust to motion blur photographs.
</div>
</div>

[comment]: <> (**Shiyu Jiang**, Junjie Jia, Yi Yuan, Yuxiong Wu, Tianqi Wang. [Research on China’s Primary Industry: Evidence From Regional Analysis Based on SVM and Moran’s Index]&#40;https://ieeexplore.ieee.org/abstract/document/9754653&#41;)

[comment]: <> (. *International Conference on Cloud Computing and Intelligent Systems*, 2021.)

[comment]: <> (- This article aims to use machine learning and Moran’s I to analyze the current situation of China’s primary industry from a regional perspective.)

[comment]: <> (# 🎖 Honors and Awards)

[comment]: <> (- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. )

[comment]: <> (- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. )


# 🧑‍💻 Software
## Research Pipeline & Model
[comment]: <> (- [Nano-plastic ML Detector]&#40;&#41;:)
- [Nano-plastics ML](https://github.com/Haoxin01/Nanoplastics-ML): This work applies machine learning to forecast types and concentrations of nanoplastics in the environment.
- [Koudou: An Agent-based Model for Epidemic Simulation](https://github.com/caranha/Koudou/tree/ALIFE_2023): 
  This agent-based model analyzes the impact of masking and large-scale evacuations on human mobility within a university campus and its neighborhood.
- [RNA-seq & ChIP-seq Joint Analysis Pipeline](https://github.com/JasonJiangs/RNAseq-ChIPseq-Joint-Pipeline): 
  This pipeline integrates RNA-seq and ChIP-seq tools for analyzing transcriptional regulation, configured easily through YAML files and command-line arguments.

## Web server
- [HNOXPred](https://github.com/JasonJiangs/HNOX_Pred) (**Pred**iction of **H**eme-**N**itric oxide/**OX**ygen domains):
  This web server predicts gas-sensing H-NOX proteins from amino acid sequences, returning H-NOX centers and scores scaled from 0 to 1 based on comparisons to the HNOXPred database.
- [Koudou Simulator Analyser](https://github.com/caranha/Koudou/tree/ALIFE_2023/src/dashapp):
  This web tool provides statistical, geographical, and visualization analysis of infectious disease simulations for the Koudou Simulator, allowing comparative analysis.

## Full-stack
- [OfficeAdmin](https://github.com/JasonJiangs/OfficeAdmin): An office management system developed by Spring Boot, MyBatis-Plus, Redis, MySQL, etc.
- [Microservice](https://github.com/JasonJiangs/Microservice): The project implements several small scripts and microservices using Golang and its frameworks.

# 🌎 Miscellaneous
Soccer (Visca Barça~), Gym, Table tennis, Piano, Traveling, etc.


<body>
  <a href="https://clustrmaps.com/site/1bt6x"  title="Visit tracker" >
    <img src="//www.clustrmaps.com/map_v2.png?d=aGpjzbKbHZT-5oLEhHvcK0igPnT7IvQmYxySQX6oPb4&cl=ffffff" />
  </a>
</body>