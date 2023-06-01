<div class="markdown-body"><h1>Face Recognition</h1>
<p>This project is a demo based on <a href="https://github.com/serengil/deepface">DeepFace</a>.</p>
<h2>Installation</h2>
<p>To use this project, you will need to install the following dependencies:</p>
<pre class="code-block-wrapper"><div class="code-block-header"><span class="code-block-header__lang"></span><span class="code-block-header__copy"></span></div><code class="hljs code-block-body ">pip <span class="hljs-keyword">install</span> tensorflow
pip <span class="hljs-keyword">install</span> deepface
</code></pre>
<h2>Usage</h2>
<p>The project includes the following files for face detection and recognition:</p>
<ul>
<li><code>face_detection.py</code>: Face detection and alignment.</li>
<li><code>face_rec_find.py</code>: Face recognition using the <code>find</code> method.</li>
<li><code>face_rec_verify.py</code>: Face recognition using the <code>verify</code> method.</li>
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
<h3>Running the Demo</h3>
<p>To run the demo, simply place your photo in the <code>database/person</code> directory, and then run either <code>face_rec_find.py</code> or <code>face_rec_verify.py</code>.</p>
<p>Notes:</p>
<ul>
<li><code>face_rec_find.py</code> assumes the default directory for face recognition data is <code>database</code>. If you put your photos in the <code>database/person</code> directory and run the file, it will recognize your face.</li>
<li><code>face_rec_verify.py</code> requires that you change the <code>reference_img</code> path to your photo's path before running the file.</li>
</ul>
</div>
