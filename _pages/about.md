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
Hi! my name is Shiyu Jiang. I am currently a PhD student in computer science at the University of Florida working 
with [Prof. Yanjun Li](https://pharmacy.ufl.edu/profile/li-yanjun/) and [Prof. Matthew Disney](https://wertheim.scripps.ufl.edu/profile/disney-matthew/#page).
My research lies at the intersection of AI and biology, where I design computational approaches to accelerate discoveries 
in synthetic biology, drug discovery, and molecular interaction. Specifically, I primarily focus on those areas: <br>

- <button type="button" class="ra-trigger" data-ra-target="ra-modal-drug" aria-haspopup="dialog">AI-driven drug discovery<span class="ra-trigger__count">3 papers</span></button>: generative modeling and representation learning for molecular prediction, sequence design, and optimization; drug-induced cellular phenotype prediction; and structural data resources for ligand recognition.
- <button type="button" class="ra-trigger" data-ra-target="ra-modal-lm" aria-haspopup="dialog">Foundation models for life sciences<span class="ra-trigger__count">8 papers</span></button>: single-cell foundation models and language models for protein and nucleic acid sequences, spanning model development, evaluation, and applications.
- <button type="button" class="ra-trigger" data-ra-target="ra-modal-exp" aria-haspopup="dialog">Experiment-driven protein and cellular engineering<span class="ra-trigger__count">7 papers</span></button>: building the computational core of wet-lab campaigns, from sequence–activity landscape modeling to variant prioritization for enzyme and Cas nuclease evolution.
- Agentic systems, memory, and continual learning: parametric and non-parametric memory, long-horizon adaptation, self-evolving agents, reinforcement learning, and agentic systems for scientific discovery.

Before starting my PhD, I was very fortunate to work with and learn from really brilliant, inspiring mentors and collaborators 
across these fields, you can find them in the experience panel. 

<div class="ra-modal" id="ra-modal-drug" role="dialog" aria-modal="true" aria-labelledby="ra-modal-drug-title">
  <div class="ra-modal__backdrop" data-ra-close></div>
  <div class="ra-modal__panel">
    <button type="button" class="ra-modal__close" data-ra-close aria-label="Close">&times;</button>
    <h3 class="ra-modal__title" id="ra-modal-drug-title">AI-driven drug discovery</h3>
    <p class="ra-modal__note">Related work, most recent first.</p>
    <ul class="ra-reflist">
      <li><strong>Jiang, S.</strong>, Yang, Z., Taghavi, A., Wei, J., Childs-Disney, J. L., Li, C., Disney, M. D., &amp; Li, Y. (2026). SMARTFlexDB: A database of paired apo&#8211;holo RNA structures for analyzing conformational remodeling and small-molecule recognition. In preparation. <a href="https://aidd.rc.ufl.edu/app/smartflexdb/">https://aidd.rc.ufl.edu/app/smartflexdb/</a></li>
      <li><strong>Jiang, S.</strong>&#8224;, Taghavi, A.&#8224;, Wang, T., Sung, K., Meyer, S. M., Springer, N. A., Wei, J., Childs-Disney, J. L., Li, C., Disney, M. D., &amp; Li, Y. (2026). Small molecule approach to RNA targeting binder discovery (SMARTBind) using deep learning without structural input [Preprint]. <em>bioRxiv</em>. Under review at <em>Nature Portfolio</em>. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12485756/">https://pmc.ncbi.nlm.nih.gov/articles/PMC12485756/</a></li>
      <li>Zheng, X., <strong>Jiang, S.</strong>, Seabra, G., Li, C., &amp; Li, Y. (2026). Apo2Mol: 3D molecule generation via dynamic pocket-aware diffusion models. <em>Proceedings of the AAAI Conference on Artificial Intelligence</em>. <a href="https://ojs.aaai.org/index.php/AAAI/article/view/37138">https://ojs.aaai.org/index.php/AAAI/article/view/37138</a></li>
    </ul>
    <p class="ra-modal__footnote">&#8224; Equal contribution.</p>
  </div>
</div>

<div class="ra-modal" id="ra-modal-lm" role="dialog" aria-modal="true" aria-labelledby="ra-modal-lm-title">
  <div class="ra-modal__backdrop" data-ra-close></div>
  <div class="ra-modal__panel">
    <button type="button" class="ra-modal__close" data-ra-close aria-label="Close">&times;</button>
    <h3 class="ra-modal__title" id="ra-modal-lm-title">Foundation models for life sciences</h3>
    <p class="ra-modal__note">Related work, most recent first.</p>
    <ul class="ra-reflist">
      <li><strong>Jiang, S.</strong>&#8224;, Fang, Z.&#8224;, Zhang, Y., Zhang, X., Kalfon, J., Wang, W., . . . Ding, J. (2026). The landscape of single-cell foundation models: Design principles, applications, and open challenges [Manuscript submitted for publication, under review]. <a href="https://github.com/OmicsML/awesome-foundation-model-single-cell-papers">https://github.com/OmicsML/awesome-foundation-model-single-cell-papers</a></li>
      <li>Ding, J.&#8224;, Lin, J.&#8224;, Miao, Z.&#8224;, Mechtel, N.&#8224;, <strong>Jiang, S.</strong>, Wang, Y., Fang, Z., Martin-Rufino, J. D., Weng, C., Saunders, R., Xu, W., Weissman, J. S., Ouyang, W., Li, M., Tang, J., Lu, Y. R., &amp; Qiu, X. (2026). Predictive single cell foundation model for gene regulation and aging with privacy-preserving tabular learning [Preprint]. <em>arXiv</em>. <a href="https://arxiv.org/abs/2607.19400">https://arxiv.org/abs/2607.19400</a></li>
      <li>Zhou, X.&#8224;, Han, C.&#8224;, Zhang, Y.&#8224;, Du, H.&#8224;, Tian, J.&#8224;, Su, J.&#8225;, Liu, R.&#8225;, Zhuang, K.&#8225;, <strong>Jiang, S.</strong>&#8225;, Gitter, A., . . . Yuan, F. (2026). Decoding the molecular language of proteins with Evolla [Preprint]. <em>bioRxiv</em>. <a href="https://www.biorxiv.org/content/10.1101/2025.01.05.630192v4.full.pdf">https://doi.org/10.1101/2025.01.05.630192</a></li>
      <li><strong>Jiang, S.</strong>, Liu, X., &amp; Wang, J. Z. (2026). Evaluating DNA function understanding in genomic language models using evolutionarily implausible sequences. <em>ACS Synthetic Biology</em>. <a href="https://pubs.acs.org/doi/10.1021/acssynbio.6c00024">https://doi.org/10.1021/acssynbio.6c00024</a></li>
      <li>Su, J.&#8224;, He, Y.&#8224;, You, S.&#8224;, <strong>Jiang, S.</strong>, Zhou, X., Zhang, X., Wang, Y., Su, X., Tolstoy, I., Chang, X., Lu, H., &amp; Yuan, F. (2025). A tri-modal protein language model enables advanced protein searches. <em>Nature Biotechnology</em>. <a href="https://www.nature.com/articles/s41587-025-02836-0">https://doi.org/10.1038/s41587-025-02836-0</a></li>
      <li>Su, J., Li, Z., Tao, T., Han, C., He, Y., Dai, F., Yuan, Q., Gao, Y., Si, T., Zhang, X., Zhou, Y., Shan, J., Zhou, X., Chang, X., <strong>Jiang, S.</strong>, Ma, D., The OPMC, Steinegger, M., Ovchinnikov, S., &amp; Yuan, F. (2025). SaprotHub: Democratizing protein language model training, sharing and collaboration for the biology community. <em>Nature Biotechnology</em>. <a href="https://www.nature.com/articles/s41587-025-02859-7">https://doi.org/10.1038/s41587-025-02859-7</a></li>
      <li>Ding, J.&#8224;, Lin, J.&#8224;, <strong>Jiang, S.</strong>&#8224;, Wang, Y., Mao, Z., Fang, Z., Tang, J., Li, M., &amp; Qiu, X. (2025). Tabula: A tabular self-supervised foundation model for single-cell transcriptomics. <em>Advances in Neural Information Processing Systems</em>. <a href="https://openreview.net/forum?id=Vk2sfKAdeu">https://openreview.net/forum?id=Vk2sfKAdeu</a></li>
      <li><strong>Jiang, S.</strong>, Liu, X., &amp; Wang, J. Z. (2025). Predicting function of evolutionarily implausible DNA sequences. <em>ICML 2025 Generative AI and Biology Workshop</em>. <a href="https://icml.cc/virtual/2025/51254">https://icml.cc/virtual/2025/51254</a></li>
    </ul>
    <p class="ra-modal__footnote">&#8224; Equal contribution. &#8225; Equal secondary contribution.</p>
  </div>
</div>

<div class="ra-modal" id="ra-modal-exp" role="dialog" aria-modal="true" aria-labelledby="ra-modal-exp-title">
  <div class="ra-modal__backdrop" data-ra-close></div>
  <div class="ra-modal__panel">
    <button type="button" class="ra-modal__close" data-ra-close aria-label="Close">&times;</button>
    <h3 class="ra-modal__title" id="ra-modal-exp-title">Experiment-driven protein and cellular engineering</h3>
    <p class="ra-modal__note">Related work, most recent first.</p>
    <ul class="ra-reflist">
      <li>Cheng, L.&#8224;, Zheng, X.&#8224;, Ding, H.&#8224;, <strong>Jiang, S.</strong>, Hu, Y., Wang, C., Li, C.-L., Tian, Z., Leeuwon, R. J., Rui, J., Ye, H., Yuan, T., Liu, Y., Yang, K., Zhou, B., Huang, X., &amp; Xiao, H. (2026). Sequence Display generates large-scale sequence&#8211;activity datasets for reprogramming SlugCas9 toward difficult-to-access PAMs. <em>Nature Communications</em>. Accepted in principle.</li>
      <li>Cheng, L.&#8224;, Zheng, X.&#8224;, <strong>Jiang, S.</strong>&#8224;, Hu, Y., Liu, Y., Yang, K., Rui, J., Ding, H., Zhang, M., Yuan, T., Ye, H., Li, C., Yang, K. K., Huang, X., &amp; Xiao, H. (2026). Sequence Display: Generating large-scale sequence&#8211;activity datasets to advance universal protein evolution. <em>Nature Biotechnology</em>. <a href="https://www.nature.com/articles/s41587-026-03087-3">https://doi.org/10.1038/s41587-026-03087-3</a></li>
      <li>Yuan, T., Zhang, M., Cheng, L., Zheng, X., <strong>Jiang, S.</strong>, Huang, X., &amp; Xiao, H. (2025). Biocatalytic synthesis of N-protected &#945;-amino acids through 1,3-nitrogen migration by nonheme iron enzymes. <em>Journal of the American Chemical Society</em>, 147(48), 44041&#8211;44047. <a href="https://pubs.acs.org/doi/10.1021/jacs.5c11008">https://doi.org/10.1021/jacs.5c11008</a></li>
      <li>Hu, Y., Wang, Yixian, Cheng, L., Wang, C., Liu, Y., Wang, Yufei, Chen, Y., Yang, S., Guo, Y., <strong>Jiang, S.</strong>, Yang, K., &amp; Xiao, H. (2025). Engineering unnatural cells with a 21st amino acid as a living epigenetic sensor. <em>Nature Communications</em>, 16, 9388. <a href="https://www.nature.com/articles/s41467-025-64448-1">https://doi.org/10.1038/s41467-025-64448-1</a></li>
      <li>Hu, Y.&#8224;, Cheng, L.&#8224;, Liu, Y., Liu, R., <strong>Jiang, S.</strong>, Yuan, T., Wang, Y., Ye, H., &amp; Xiao, H. (2025). Biosynthesis of unnatural cyclodipeptides through genetic code expansion and cyclodipeptide synthase evolution. <em>Journal of the American Chemical Society</em>. <a href="https://pubs.acs.org/doi/10.1021/jacs.5c08627">https://doi.org/10.1021/jacs.5c08627</a></li>
      <li>Guo, Y.&#8224;, Cheng, L.&#8224;, Hu, Y., Zhang, M., Liu, R., Wang, Y., <strong>Jiang, S.</strong>, &amp; Xiao, H. (2024). Biosynthesis of halogenated tryptophans for protein engineering using genetic code expansion. <em>ChemBioChem</em>, 25(20), e202400366. <a href="https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cbic.202400366">https://doi.org/10.1002/cbic.202400366</a></li>
      <li>Ye, H., <strong>Jiang, S.</strong>, Yan, Y., Zhao, B., Grant, E. R., Kitts, D. D., Yada, R. Y., Pratap-Singh, A., Baldelli, A., &amp; Yang, T. (2024). Integrating metal&#8211;phenolic networks-mediated separation and machine learning-aided surface-enhanced Raman spectroscopy for accurate nanoplastics quantification and classification. <em>ACS Nano</em>. <a href="https://pubs.acs.org/doi/abs/10.1021/acsnano.4c08316">https://doi.org/10.1021/acsnano.4c08316</a></li>
    </ul>
    <p class="ra-modal__footnote">&#8224; Equal contribution.</p>
  </div>
</div>

<script>
(function () {
  var openModal = null;
  var lastTrigger = null;

  function close() {
    if (!openModal) return;
    openModal.classList.remove('is-open');
    document.body.classList.remove('ra-modal-open');
    openModal = null;
    if (lastTrigger) lastTrigger.focus();
  }

  function open(modal, trigger) {
    close();
    modal.classList.add('is-open');
    document.body.classList.add('ra-modal-open');
    openModal = modal;
    lastTrigger = trigger || null;
    var closeBtn = modal.querySelector('.ra-modal__close');
    if (closeBtn) closeBtn.focus();
  }

  document.addEventListener('click', function (e) {
    var trigger = e.target.closest('.ra-trigger');
    if (trigger) {
      var modal = document.getElementById(trigger.getAttribute('data-ra-target'));
      if (modal) { e.preventDefault(); open(modal, trigger); }
      return;
    }
    if (e.target.closest('[data-ra-close]')) { e.preventDefault(); close(); }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') close();
  });
})();
</script>

# 📖 Educations
- *2026 - Present*, PhD student, Computer Science. University of Florida. *Gainesville, FL*
- *2025 - 2026*, PhD student, Computational Biology and Bioinformatics. University of Southern California. *Los Angeles, CA*
- *2022 - 2024*, Master of Science in Engineering, Computer Science. Johns Hopkins University. *Baltimore, MD* 
- *2018 - 2022*, Bachelor of Science, Computer Science. Wenzhou-Kean University. *Wenzhou, China*

# 📰 News
<!-- - *2026.08*: One first authored paper "SMARTFlexDB: a database of paired apo-holo RNA structures for analyzing conformational remodeling and small-molecule recognition" is released on ***[bioRxiv]()***. -->
<!-- - *2026.08*: One first authored paper "The landscape of single-cell foundation models: design principles, applications, and open challenges" is released on ***[arXiv]()***. -->
- *2026.08*: One co-authored paper "Sequence Display generates large-scale sequence-activity datasets for reprogramming SlugCas9 toward difficult-to-access PAMs" is accepted by ***[Nature Communications]()***!
<!-- - *2026.08*: One first authored paper "Small Molecule Approach to RNA Targeting Binder Discovery (SMARTBind) Using Deep Learning Without Structural Input" is accepted by ***[Nature Communications]()***! -->
- *2026.07*: One co-authored paper "Predictive single cell foundation model for gene regulation and aging with privacy-preserving tabular learning" is released on [arXiv](https://arxiv.org/abs/2607.19400). Check out our [post](https://x.com/Xiaojie_Qiu/status/2077456094696456192).
- *2026.05*: One first authored paper "Evaluating DNA function understanding in genomic language models using evolutionarily implausible sequences" is accepted by ***[ACS Synthetic Biology](https://pubs.acs.org/doi/10.1021/acssynbio.6c00024)***!
- *2026.05*: Our sequence display paper is featured as a research highlight in ***[Nature Methods](https://www.nature.com/articles/s41592-026-03106-w)*** and [Rice News](https://news.rice.edu/news/2026/scientists-uncover-new-method-generate-protein-datasets-training-ai)!
- *2026.02*: One co-first authored paper "Sequence Display: Generating Large-Scale Sequence–Activity Datasets to Advance Universal Protein Evolution" is accepted by ***[Nature Biotechnology](https://www.nature.com/articles/s41587-026-03087-3)***!

<details>
<summary><strong>Earlier News (Click to Expand)</strong></summary>

<div markdown="1">

- *2026.01*: "Small Molecule Approach to RNA Targeting Binder Discovery (SMARTBind) Using Deep Learning Without Structural Input" is presented at ***[UF Health Cancer Institute Annual Research Showcase 2026](https://cancer.ufl.edu/education/research-showcase/)***, see our [poster](https://jasonjiangs.github.io/images/UFHCI-Poster.png).
- *2025.11*: One co-authored paper "Apo2Mol: 3D Molecule Generation via Dynamic Pocket-Aware Diffusion Models" is accepted by ***[AAAI 2026](https://arxiv.org/abs/2511.14559)***!
- *2025.10*: One co-authored paper "Engineering Unnatural Cells with a 21st Amino Acid as a Living Epigenetic Sensor" is on ***[Nature Communications](https://www.nature.com/articles/s41467-025-64448-1)***!
- *2025.09*: One first-authored paper "Small Molecule Approach to RNA Targeting Binder Discovery (SMARTBind) Using Deep Learning Without Structural Input" is released on [bioRxiv](https://www.biorxiv.org/content/10.1101/2025.09.24.678312v1).
- *2025.09*: One co-first authored paper "Tabula: A Tabular Self-Supervised Foundation Model for Single-Cell Transcriptomics" is accepted by ***[NeurIPS 2025](https://openreview.net/forum?id=Vk2sfKAdeu)***!
- *2025.09*: One co-authored paper "Biosynthesis of Unnatural Cyclodipeptides through Genetic Code Expansion and Cyclodipeptide Synthase Evolution" is on ***[Journal of the American Chemical Society](https://doi.org/10.1021/jacs.5c08627)***!
- *2025.08*: One co-authored paper "SaprotHub: Democratizing Protein Language Model Training, Sharing and Collaboration for the Biology Community" is accepted by ***[Nature Biotechnology](https://www.nature.com/articles/s41587-025-02859-7)***!
- *2025.07*: One co-authored paper "A tri-modal protein language model enables advanced protein searches" is accepted by ***[Nature Biotechnology](https://www.nature.com/articles/s41587-025-02836-0)***!
- *2025.07*: "Predicting function of evolutionarily implausible DNA sequences" is presented at [Q-BIO 2025 Conference: Emergent Orders in Living Systems Across Scales](https://cqb.pku.edu.cn/info/1064/3011.htm), see our [poster](https://jasonjiangs.github.io/images/nullsettes_poster.png).
- *2025.06*: "Sequence Display-Enabled Machine Learning for Protein Evolution" is presented at [2025 Synthetic Biology: Engineering, Evolution, & Design](https://aiche.confex.com/aiche/seed2025/meetingapp.cgi/Paper/708439), see our [poster](https://jasonjiangs.github.io/images/seq_display_poster.png).
- *2025.06*: One first authored paper "Predicting function of evolutionarily implausible DNA sequences" is accepted by ***[ICML 2025 Generative AI and Biology Workshop](https://icml.cc/virtual/2025/51254)***!
- *2025.04*: I will be joining the PhD program in Computational Biology and Bioinformatics at [USC QCB](https://www.qcb-dornsife.usc.edu/), looking forward to the journey.
- *2025.01*: "Toward a privacy-preserving predictive foundation model of single-cell transcriptomics with federated learning and tabular modeling" is released on [bioRxiv](https://www.biorxiv.org/content/10.1101/2025.01.06.631427v1), see our [post](https://x.com/Xiaojie_Qiu/status/1876676759577661895).

</div>

</details>

# 📝 Selected Publications

<button id="toggleAllBtn" onclick="toggleAllPublications()" style="background-color: transparent; border: none; cursor: pointer; font-size: 0.9em; font-weight: bold; padding: 0; color: inherit;">Click to Close All</button>

<script>
function toggleAllPublications() {
  const details = document.querySelectorAll('details[data-publications]');
  const btn = document.getElementById('toggleAllBtn');
  const allOpen = Array.from(details).every(d => d.hasAttribute('open'));
  
  details.forEach(d => {
    if (allOpen) {
      d.removeAttribute('open');
    } else {
      d.setAttribute('open', '');
    }
  });
  
  btn.textContent = allOpen ? 'Click to Open All' : 'Click to Close All';
}
</script>

<details open data-publications>
<summary><span style="font-size: 1.3em; font-weight: bold; !important">2026</span></summary>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">In preparation</div><img src='images/smartflexdb.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

SMARTFlexDB: a database of paired apo-holo RNA structures for analyzing conformational remodeling and small-molecule recognition

**Shiyu Jiang**, Zekun Yang, Amirhossein Taghavi, Jinhang Wei, Jessica L. Childs-Disney, Chenglong Li, Mattew D. Disney, Yanjun Li. 2026. (In preparation)

<div class="paper-link-buttons">
  <a href="https://aidd.rc.ufl.edu/app/smartflexdb/">Database</a>
</div>
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv</div><img src='images/scfm_review.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[The landscape of single-cell foundation models: design principles, applications, and open challenges]()

**Shiyu Jiang** †, Zhaoyu Fang †, York Zhang, Xuting Zhang, Jérémie Kalfon, Weixu Wang, ..., Fei Wang, Yuying Xie, Jiliang Tang, Raul Rabadan, David van Dijk, Pengtao Xie, Peng He, Emily Fox, Le Song, Fabian J. Theis, Eric Xing, Christina V. Theodoris, Xiaojie Qiu, Jiayuan Ding. 2026. (Under Review)

<div class="paper-link-buttons">
  <a class="star-badge" href="https://github.com/OmicsML/awesome-foundation-model-single-cell-papers"><img src="https://img.shields.io/github/stars/OmicsML/awesome-foundation-model-single-cell-papers?style=social&amp;label=Code+Stars" alt="Code Stars" height="20" loading="lazy"></a>
</div>
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv</div><img src='images/tabula_v2.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[Predictive single cell foundation model for gene regulation and aging with privacy-preserving tabular learning](https://arxiv.org/abs/2607.19400)

Jiayuan Ding †, Jianhui Lin †, Ziyang Miao †, Nils Mechtel †, **Shiyu Jiang**, Yixin Wang, Zhaoyu Fang, Jorge D. Martin-Rufino, Chen Weng, Reuben Saunders, Weize Xu, Jonathan S. Weissman, Wei Ouyang, Min Li, Jiliang Tang, Yuancheng Ryan Lu, Xiaojie Qiu. *arXiv*, 2026. (Under Review at ***Nature Portfolio***)

<div class="paper-link-buttons">
  <a class="star-badge" href="https://github.com/aristoteleo/tabula"><img src="https://img.shields.io/github/stars/aristoteleo/tabula?style=social&amp;label=Code+Stars" alt="Code Stars" height="20" loading="lazy"></a>
  <span class="citation-button show_paper_citations" data-paper-id="TchSd_cAAAAJ:R3hNpaxXUhUC">Citations</span>
  <a href="https://chiron.aicell.io/">Chiron platform</a>
</div>
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">bioRxiv</div><img src='images/evolla.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[Decoding the Molecular Language of Proteins with Evolla](https://www.biorxiv.org/content/10.1101/2025.01.05.630192v4.full.pdf)

Xibin Zhou †, Chenchen Han †, Yinqi Zhang †, Huan Du †, Jiayuan Tian †, Jin Su ‡, Renju Liu ‡, Kai Zhuang ‡, **Shiyu Jiang** ‡, Anthony Gitter, ..., Zongze Zhao, Yang Liu, Hongyuan Lu, Fajie Yuan. *bioRxiv*, 2026. (Under Review at ***Nature Portfolio***)

<div class="paper-link-buttons">
  <a class="star-badge" href="https://github.com/westlake-repl/Evolla"><img src="https://img.shields.io/github/stars/westlake-repl/Evolla?style=social&amp;label=Code+Stars" alt="Code Stars" height="20" loading="lazy"></a>
  <span class="citation-button show_paper_citations" data-paper-id="TchSd_cAAAAJ:kNdYIx-mwKoC">Citations</span>
</div>
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">bioRxiv</div><img src='images/smartbind.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[Small Molecule Approach to RNA Targeting Binder Discovery (SMARTBind) Using Deep Learning Without Structural Input](https://pmc.ncbi.nlm.nih.gov/articles/PMC12485756/)

**Shiyu Jiang** †, Amirhossein Taghavi †, Tenghui Wang, Kisu Sung, Samantha M. Meyer, Noah A. Springer, Jinhang Wei, Jessica L. Childs-Disney, Chenglong Li, Mattew D. Disney, Yanjun Li. *bioRxiv*, 2026. (Under Review at ***Nature Portfolio***)

<div class="paper-link-buttons">
  <a class="star-badge" href="https://github.com/AIDD-LiLab/SMARTBind"><img src="https://img.shields.io/github/stars/AIDD-LiLab/SMARTBind?style=social&amp;label=Code+Stars" alt="Code Stars" height="20" loading="lazy"></a>
  <span class="citation-button show_paper_citations" data-paper-id="TchSd_cAAAAJ:qxL8FJ1GzNcC">Citations</span>
</div>
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Nature Communications</div><img src='images/SD_v2.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[Sequence Display generates large-scale sequence-activity datasets for reprogramming SlugCas9 toward difficult-to-access PAMs]()

Linqi Cheng †, Xinzhe Zheng †, Haoxue Ding †, **Shiyu Jiang**, Yu Hu, Chenhang Wang, Chen-Long Li, Zuotong Tian, Rain Jay Leeuwon, Jinyan Rui, Haoxin Ye, Teng Yuan, Yijie Liu, Kaiqiang Yang, Boyang Zhou, Xiongyi Huang, Han Xiao. *Nature Communications*, 2026. (Accepted in principle)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACS Synthetic Biology</div><img src='images/nullsettes_v2.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[Evaluating DNA function understanding in genomic language models using evolutionarily implausible sequences](https://pubs.acs.org/doi/10.1021/acssynbio.6c00024)

**Shiyu Jiang**, Xuyin Liu, Jerry Zitong Wang. *ACS Synthetic Biology*, 2026.

<div class="paper-link-buttons">
  <a class="star-badge" href="https://github.com/cellethology/GLM-Nullsette-Benchmark"><img src="https://img.shields.io/github/stars/cellethology/GLM-Nullsette-Benchmark?style=social&amp;label=Code+Stars" alt="Code Stars" height="20" loading="lazy"></a>
  <span class="citation-button show_paper_citations" data-paper-id="TchSd_cAAAAJ:TQgYirikUcIC">Citations</span>
  <a href="https://jasonjiangs.github.io/images/nullsettes_poster.png">Poster</a>
</div>
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Nature Biotechnology</div><img src='images/sequence display.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[Sequence Display: Generating Large-Scale Sequence–Activity Datasets to Advance Universal Protein Evolution](https://www.nature.com/articles/s41587-026-03087-3)

Linqi Cheng †, Xinzhe Zheng †, **Shiyu Jiang** †, Hu Y, Liu Y, Yang K, Rui J, Ding H, Zhang M, Yuan T, Ye H, Li C, Kevin K. Yang, Xiongyi Huang, Han Xiao. *Nature Biotechnology*, 2026.

<div class="paper-link-buttons">
  <a class="star-badge" href="https://github.com/SophieSarceau/SequenceDisplay-ML"><img src="https://img.shields.io/github/stars/SophieSarceau/SequenceDisplay-ML?style=social&amp;label=Code+Stars" alt="Code Stars" height="20" loading="lazy"></a>
  <span class="citation-button show_paper_citations" data-paper-id="TchSd_cAAAAJ:mB3voiENLucC">Citations</span>
  <a href="https://jasonjiangs.github.io/images/seq_display_poster.png">Poster</a>
  <a href="https://www.nature.com/articles/s41592-026-03106-w">Nature Methods Research Highlights</a>
  <a href="https://www.eurekalert.org/news-releases/1123906">EurekAlert!</a>
  <a href="https://phys.org/news/2026-04-protein-breakthrough-generates-10m-turbocharges.html">Phys.org</a>
  <a href="https://www.news-medical.net/news/20260413/New-method-boosts-AI-driven-protein-engineering-with-massive-data.aspx">The Medical New</a>
  <a href="https://www.miragenews.com/scientists-discover-new-ai-protein-dataset-1654452/">Mirage News</a>
</div>
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2026</div><img src='images/apo2mol.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[Apo2Mol: 3D Molecule Generation via Dynamic Pocket-Aware Diffusion Models](https://ojs.aaai.org/index.php/AAAI/article/view/37138)

Xinzhe Zheng, **Shiyu Jiang**, Gustavo Seabra, Chenglong Li, Yanjun Li. *AAAI (poster)*, 2026.

<div class="paper-link-buttons">
  <a class="star-badge" href="https://github.com/AIDD-LiLab/Apo2Mol"><img src="https://img.shields.io/github/stars/AIDD-LiLab/Apo2Mol?style=social&amp;label=Code+Stars" alt="Code Stars" height="20" loading="lazy"></a>
  <span class="citation-button show_paper_citations" data-paper-id="TchSd_cAAAAJ:IWHjjKOFINEC">Citations</span>
</div>
</div>
</div>

</details>

<details open data-publications>
<summary><span style="font-size: 1.3em; font-weight: bold; !important">2025</span></summary>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/tabula_nips.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[Tabula: A Tabular Self-Supervised Foundation Model for Single-Cell Transcriptomics](https://openreview.net/forum?id=Vk2sfKAdeu)

Jiayuan Ding †, Jianhui Lin †, **Shiyu Jiang** †, Yixin Wang, Ziyang Mao, Zhaoyu Fang, Jiliang Tang, Min Li, Xiaojie Qiu. *NeurIPS* (poster), 2025.

<div class="paper-link-buttons">
  <a class="star-badge" href="https://github.com/aristoteleo/tabula"><img src="https://img.shields.io/github/stars/aristoteleo/tabula?style=social&amp;label=Code+Stars" alt="Code Stars" height="20" loading="lazy"></a>
  <span class="citation-button show_paper_citations" data-paper-id="TchSd_cAAAAJ:hFOr9nPyWt4C">Citations</span>
</div>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">JACS</div><img src='images/jacs_1.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[Biosynthesis of Unnatural Cyclodipeptides through Genetic Code Expansion and Cyclodipeptide Synthase Evolution](https://pubs.acs.org/doi/10.1021/jacs.5c08627)

Hu Y †, Cheng L †, Liu Y, Liu R, **Jiang S**, Yuan T, Wang Y, Ye H, Xiao H. *Journal of the American Chemical Society*, 2025.

<div class="paper-link-buttons">
  <a class="star-badge" href="https://github.com/linqicheng-xiao/gmx_mmpbsa_py"><img src="https://img.shields.io/github/stars/linqicheng-xiao/gmx_mmpbsa_py?style=social&amp;label=Code+Stars" alt="Code Stars" height="20" loading="lazy"></a>
  <span class="citation-button show_paper_citations" data-paper-id="TchSd_cAAAAJ:M3ejUd6NZC8C">Citations</span>
</div>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Nature Biotechnology</div><img src='images/protrek.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[A tri-modal protein language model enables advanced protein searches](https://www.nature.com/articles/s41587-025-02836-0)

Jin Su †, Yan He †, Shiyang You †, **Shiyu Jiang**, Xibin Zhou, Xuting Zhang, Yuxuan Wang, Xining Su, Igor Tolstoy, Xing Chang, Hongyuan Lu, Fajie Yuan. *Nature Biotechnology*, 2025.

<div class="paper-link-buttons">
  <a class="star-badge" href="https://github.com/westlake-repl/ProTrek"><img src="https://img.shields.io/github/stars/westlake-repl/ProTrek?style=social&amp;label=Code+Stars" alt="Code Stars" height="20" loading="lazy"></a>
  <span class="citation-button show_paper_citations" data-paper-id="TchSd_cAAAAJ:4DMP91E08xMC">Citations</span>
  <a href="http://search-protrek.com/">Online Server</a>
</div>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Nature Biotechnology</div><img src='images/saprothub.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[SaprotHub: Democratizing Protein Language Model Training, Sharing and Collaboration for the Biology Community](https://www.nature.com/articles/s41587-025-02859-7)

Jin Su, Zhikai Li, Tianli Tao, Chenchen Han, Yan He, Fengyuan Dai, Qingyan Yuan, Yuan Gao, Tong Si, Xuting Zhang, Yuyang Zhou, Junjie Shan, Xibin Zhou, Xing Chang, **Shiyu Jiang**, Dacheng Ma, The OPMC, Martin Steinegger, Sergey Ovchinnikov, Fajie Yuan. *Nature Biotechnology*, 2025.

<div class="paper-link-buttons">
  <a class="star-badge" href="https://github.com/westlake-repl/SaprotHub?tab=readme-ov-file"><img src="https://img.shields.io/github/stars/westlake-repl/SaprotHub?style=social&amp;label=Code+Stars" alt="Code Stars" height="20" loading="lazy"></a>
  <span class="citation-button show_paper_citations" data-paper-id="TchSd_cAAAAJ:9ZlFYXVOiuMC">Citations</span>
  <a href="https://theopmc.github.io/">OPMC</a>
</div>
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025 GenBio Workshop</div><img src='images/nullsettes.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[Predicting function of evolutionarily implausible DNA sequences](https://icml.cc/virtual/2025/51254)

**Shiyu Jiang**, Xuyin Liu, Jerry Zitong Wang. *ICML 2025 Generative AI and Biology Workshop*, 2025.

<div class="paper-link-buttons">
  <a class="star-badge" href="https://github.com/cellethology/GLM-Nullsette-Benchmark"><img src="https://img.shields.io/github/stars/cellethology/GLM-Nullsette-Benchmark?style=social&amp;label=Code+Stars" alt="Code Stars" height="20" loading="lazy"></a>
  <span class="citation-button show_paper_citations" data-paper-id="TchSd_cAAAAJ:ULOm3_A8WrAC">Citations</span>
</div>
</div>
</div>

</details>

<details open data-publications>
<summary><span style="font-size: 1.3em; font-weight: bold; !important">2024</span></summary>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACS Nano</div><img src='images/acsnano.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[Integrating Metal–Phenolic Networks-Mediated Separation and Machine Learning-Aided Surface-Enhanced Raman Spectroscopy for Accurate Nanoplastics Quantification and Classification](https://pubs.acs.org/doi/abs/10.1021/acsnano.4c08316)

Haoxin Ye, **Shiyu Jiang**, Yan Yan, Bin Zhao, Edward R Grant, David D Kitts, Rickey Y Yada, Anubhav Pratap-Singh, Alberto Baldelli, Tianxi Yang. *ACS Nano*, 2024.

<div class="paper-link-buttons">
  <span class="citation-button show_paper_citations" data-paper-id="TchSd_cAAAAJ:_FxGoFyzp5QC">Citations</span>
  <a href="https://pubs.acs.org/cms/10.1021/ancac3.2024.18.issue-38/asset/ancac3.2024.18.issue-38.xlargecover-4.jpg">Featured on Cover</a>
</div>
</div>
</div>

</details>

<details open data-publications>
<summary><span style="font-size: 1.3em; font-weight: bold; !important">2023</span></summary>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ALIFE 2023</div><img src='images/covid_sim.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[Simulating Disease Spread During Disaster Scenarios](https://direct.mit.edu/isal/proceedings/isal/35/123/116938)

**Shiyu Jiang**, Heejoong Kim, Fabio Henrique Tanaka, Claus Aranha, Anna Bogdanova, Kimia Ghobadi, Anton Dahbura. *The International Conference on Artificial Life*, 2023.

<div class="paper-link-buttons">
  <a class="star-badge" href="https://github.com/caranha/Koudou/tree/ALIFE_2023"><img src="https://img.shields.io/github/stars/caranha/Koudou?style=social&amp;label=Code+Stars" alt="Code Stars" height="20" loading="lazy"></a>
  <span class="citation-button show_paper_citations" data-paper-id="TchSd_cAAAAJ:qjMakFHDy7sC">Citations</span>
</div>
</div>
</div>

</details>

<details open data-publications>
<summary><span style="font-size: 1.3em; font-weight: bold; !important">2022</span></summary>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Bioinformatics</div><img src='images/bioinformatics2022.png' alt="sym" width="75%"></div></div>
<div class='paper-box-text' markdown="1">

[HNOXPred: a web tool for the prediction of gas-sensing H-NOX proteins from amino acid sequence](https://academic.oup.com/bioinformatics/article/38/19/4643/6673135)

**Shiyu Jiang**, Hemn Barzan Abdalla, Chuyun Bi, Yi Zhu, Xuechen Tian, Yixin Yang, Aloysius Wong. *Bioinformatics*, 2022.

<div class="paper-link-buttons">
  <a class="star-badge" href="https://github.com/JasonJiangs/HNOX_Pred"><img src="https://img.shields.io/github/stars/JasonJiangs/HNOX_Pred?style=social&amp;label=Code+Stars" alt="Code Stars" height="20" loading="lazy"></a>
  <span class="citation-button show_paper_citations" data-paper-id="TchSd_cAAAAJ:u5HHmVD_uO8C">Citations</span>
  <a href="https://www.hnoxpred.com/">Online Server</a>
</div>
</div>
</div>

</details>


[comment]: <> (# 🎖 Honors and Awards)

[comment]: <> (- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. )

[comment]: <> (- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. )

# 🧑‍💻 Experience
<ul class="education-timeline">

    <li class="timeline-item-edu">
        <div class="timeline-icon">
            <img src="images/WLU_logo.png" alt="WLU Logo">
        </div>
        <div class="timeline-content-edu">
            <p class="date">2024.08 - 2025.06</p>
            <h4 class="title">Research Associate</h4>
            <p class="date">Development and evaluation of protein/genomic language model | Advisor: <a href="https://fajieyuan.github.io/" target="_blank">Prof. Fajie Yuan</a> & <a href="https://www.cellethology.org/" target="_blank">Dr. Zitong Jerry Wang</a></p>
            <p class="school"><a href="https://en.westlake.edu.cn/" target="_blank">Westlake University</a>, School of Engineering & Center for Interdisciplinary Studies, School of Science</p>
        </div>
    </li>

    <li class="timeline-item-edu">
        <div class="timeline-icon">
            <img src="images/rice_logo.png" alt="RiceU Logo">
        </div>
        <div class="timeline-content-edu">
            <p class="date">2023 - 2025</p>
            <h4 class="title">Remote Research Assistant</h4>
            <p class="date">Protein language model driven protein evolution with sequence display | Advisor: <a href="https://xiao.rice.edu/" target="_blank">Prof. Han Xiao</a></p>
            <p class="school"><a href="https://chemistry.rice.edu/" target="_blank">Rice University</a>, Department of Chemistry</p>
        </div>
    </li>

    <li class="timeline-item-edu">
        <div class="timeline-icon">
            <img src="images/UF_logo.png" alt="UF Logo">
        </div>
        <div class="timeline-content-edu">
            <p class="date">2023 - 2025</p>
            <h4 class="title">Remote Research Assistant</h4>
            <p class="date">RNA-small molecule drug discovery and protein-molecule generation | Advisor: <a href="https://yanjun-li.com/" target="_blank">Prof. Yanjun Li</a> & <a href="https://disney.scripps.ufl.edu/" target="_blank">Prof. Matthew D. Disney</a></p>
            <p class="school"><a href="https://pharmacy.ufl.edu/" target="_blank">University of Florida</a>, College of Pharmacy & <a href="https://wertheim.scripps.ufl.edu/" target="_blank">UF Scripps Institute</a>, Department of Chemistry</p>
        </div>
    </li>

    <li class="timeline-item-edu">
        <div class="timeline-icon">
            <img src="images/STF_logo.png" alt="Stanford Logo">
        </div>
        <div class="timeline-content-edu">
            <p class="date">2023 - 2025</p>
            <h4 class="title">Remote Research Assistant</h4>
            <p class="date">Foundation model for single-cell transcriptomics | Advisor: <a href="https://www.devo-evo.com/" target="_blank">Prof. Xiaojie Qiu</a></p>
            <p class="school"><a href="https://med.stanford.edu/genetics.html?tab=proxy" target="_blank">Stanford University</a>, Department of Genetics</p>
        </div>
    </li>

    <li class="timeline-item-edu">
        <div class="timeline-icon">
            <img src="images/UVA_logo.png" alt="UVA Logo">
        </div>
        <div class="timeline-content-edu">
            <p class="date">2024.01 - 2024.07</p>
            <h4 class="title">Lab Specialist</h4>
            <p class="date">ChIP-Seq peak calling tool | Advisor: <a href="https://zanglab.github.io/index.htm" target="_blank">Prof. Chongzhi Zang</a></p>
            <p class="school"><a href="https://med.virginia.edu/genome-sciences/" target="_blank">University of Virginia</a>, Department of Genome Sciences</p>
        </div>
    </li>

    <li class="timeline-item-edu">
        <div class="timeline-icon">
            <img src="images/AlibabaCloud_logo.png" alt="Alibaba Cloud Logo">
        </div>
        <div class="timeline-content-edu">
            <p class="date">2022.06 - 2022.08</p>
            <h4 class="title">Software Engineer Intern</h4>
            <p class="school"><a href="https://www.alibabacloud.com/en?_p_lc=5" target="_blank">Alibaba Cloud</a> </p>
        </div>
    </li>

    <li class="timeline-item-edu">
        <div class="timeline-icon">
            <img src="images/WKU_logo.png" alt="WKU Logo">
        </div>
        <div class="timeline-content-edu">
            <p class="date">2021 - 2022</p>
            <h4 class="title">Undergraduate Research Assistant</h4>
            <p class="date">Bioinformatics webtool development | Advisor: <a href="https://csmt.wku.edu.cn/en/node/1777" target="_blank">Prof. Aloysius Wong</a></p>
            <p class="school"><a href="https://csmt.wku.edu.cn/en" target="_blank">Wenzhou Kean University</a>, Department of Biology</p>
        </div>
    </li>
</ul>

<!--
# 🔨 Models and Tools

<button id="toggleModelBtn" onclick="toggleAllModelTools()" style="background-color: transparent; border: none; cursor: pointer; font-size: 0.95em; font-weight: bold; padding: 0; color: inherit;">Click to Open All</button>

<details data-modeltools>
<summary><span style="font-weight: bold;">Genomics</span></summary>
<div markdown="1">

- [Tabula](https://github.com/aristoteleo/tabula):
  A privacy-preserving predictive foundation model for single-cell transcriptomics, leveraging federated learning and tabular learning.

- [Nullsettes](https://github.com/cellethology/GLM-Nullsette-Benchmark): 
  a synthetic biology benchmark simulating loss-of-function mutations via control element translocations, enabling zero-shot evaluation of genomic language models.

- [SICER 2.0](https://zanglab.github.io/SICER2/) & [Clipper dev Version](https://github.com/zanglab/SICER2/tree/sicer_dev) (**S**patial-clustering **I**dentification of **C**hIP-**E**nriched **R**egions):
  a redesigned ChIP-Seq broad peak calling data analysis method.

</div>
</details>

<details data-modeltools>
<summary><span style="font-weight: bold;">Protein</span></summary>
<div markdown="1">

- [Sequence display](https://github.com/SophieSarceau/SequenceDisplay-ML):
  a platform that integrates large‑scale sequence–activity datasets with protein language models to map activity landscapes and identify high‑performance protein variants.

- [ProTrek](http://search-protrek.com/):
  a tri-modal protein language model that jointly models protein sequence, structure and function (SSF).

- [Evolla](http://www.chat-protein.com/):
  a protein-language generative model (Protein ChatGPT) designed to decode the molecular language of proteins.

- [SaProtHub](https://github.com/westlake-repl/SaprotHub?tab=readme-ov-file):
  making Protein Modeling Accessible to All Biologists.

- [HNOXPred](https://www.hnoxpred.com/) (**Pred**iction of **H**eme-**N**itric oxide/**OX**ygen domains):
  a web server to predict gas-sensing H-NOX proteins from amino acid sequences.

</div>
</details>

<details data-modeltools>
<summary><span style="font-weight: bold;">Drug Discovery</span></summary>
<div markdown="1">

- [Apo2Mol](https://github.com/AIDD-LiLab/Apo2Mol):
  Apo2Mol is a diffusion-based molecule generation model leveraging Apo-Holo pocket dynamics.

- [SMARTBind](https://github.com/AIDD-LiLab/SMARTBind):
  SMARTBind is a structure-agnostic RNA-ligand interaction prediction method, which can be used for RNA-ligand virtual screening and binding site prediction.

</div>
</details>

<details data-modeltools>
<summary><span style="font-weight: bold;">Other</span></summary>
<div markdown="1">

- [gmx_mmpbsa_py](https://ui.adsabs.harvard.edu/abs/2025zndo..17050354C/abstract):
  an easy-to-use Python script that integrates GROMACS molecular dynamics trajectories with APBS to compute protein–ligand binding free energies using the MM/PBSA method.

- [Koudou](https://github.com/caranha/Koudou):
  an agent-based model that simulates the infectious disease spread under college town scenario.

</div>
</details>

<script>
function toggleAllModelTools() {
  const details = document.querySelectorAll('details[data-modeltools]');
  const btn = document.getElementById('toggleModelBtn');
  const allOpen = Array.from(details).every(d => d.hasAttribute('open'));
  details.forEach(d => {
    if (allOpen) d.removeAttribute('open'); else d.setAttribute('open','');
  });
  btn.textContent = allOpen ? 'Click to Open All' : 'Click to Close All';
}

// initialize button label on load
document.addEventListener('DOMContentLoaded', function() {
  const details = document.querySelectorAll('details[data-modeltools]');
  const btn = document.getElementById('toggleModelBtn');
  if (!details.length) return;
  const allOpen = Array.from(details).every(d => d.hasAttribute('open'));
  btn.textContent = allOpen ? 'Click to Close All' : 'Click to Open All';
});
</script>
-->

# 📝 Service
- **Journal reviewer**: IEEE Transactions on Computational Biology and Bioinformatics, PLoS Computational Biology;
- **Conference reviewer**: AAAI 2026 2027, NeurIPS 2026;


# 🌎 Miscellaneous
Outside of work, you’ll often find me at gym, playing soccer, road cycling, or go hiking. 
I also enjoy playing table tennis and the piano occasionally.

