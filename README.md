<div class="markdown-body"><h1>Face Recognition</h1>
<p>This project is a demo based on <a href="https://github.com/serengil/deepface">deepface</a></p>
<h2>Installation</h2>
<p>To install the dependencies, run the following commands:</p>
<pre class="code-block-wrapper"><div class="code-block-header"><span class="code-block-header__lang"></span><span class="code-block-header__copy"></span></div><code class="hljs code-block-body bash">pip install tensorflow
pip install deepface
</code></pre>
<h2>Usage</h2>
<p>This demo includes the following files:</p>
<ul>
<li><code>face_detection.py</code>: Face detection and alignment</li>
<li><code>face_rec_find.py</code>: Multi-face recognition</li>
<li><code>face_rec_verify.py</code>: Single-face recognition</li>
</ul>
<h3>Dataset</h3>
<p>The dataset is organized as follows:</p>
<pre class="code-block-wrapper"><div class="code-block-header"><span class="code-block-header__lang"></span><span class="code-block-header__copy"></span></div><code class="hljs code-block-body ">database
├── perso<span class="hljs-symbol">n1</span>
│   ├── perso<span class="hljs-symbol">n1</span>_<span class="hljs-number">1.</span>jpg
│   └── perso<span class="hljs-symbol">n1</span>_<span class="hljs-number">2.</span>jpg
└── perso<span class="hljs-symbol">n2</span>
    └── perso<span class="hljs-symbol">n2</span>_<span class="hljs-number">1.</span>jpg
</code></pre>
<h3>Instructions</h3>
<p>To use this demo, put your photos in the <code>database/person</code> directory and run <code>face_rec_find.py</code> or <code>face_rec_verify.py</code>.</p>
<p>Note:</p>
<ul>
<li><code>face_rec_find.py</code> by default looks for the face recognition data in the <code>database</code> directory. Simply add your photos to the directory and run the file to recognize them.</li>
<li>In <code>face_rec_verify.py</code>, you need to change the <code>reference_img</code> variable to your photo's path before running the file.</li>
</ul>
</div>
