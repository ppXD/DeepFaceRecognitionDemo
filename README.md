<div class="markdown-body"><h1>Face Recognition</h1>
<p>This is a demo project built on top of <a href="https://github.com/serengil/deepface">DeepFace</a>.</p>
<h2>Installation</h2>
<p>To use this project, you need to install the following dependencies:</p>
<pre class="code-block-wrapper"><div class="code-block-header"><span class="code-block-header__lang"></span><span class="code-block-header__copy"></span></div><code class="hljs code-block-body ">pip <span class="hljs-keyword">install</span> tensorflow
pip <span class="hljs-keyword">install</span> deepface
</code></pre>
<h2>Description</h2>
<p>This project contains two modules:</p>
<ul>
<li><code>face_detection.py</code>: This module is responsible for detecting faces in images.</li>
<li><code>face_recognition.py</code>: This module is responsible for recognizing faces in images.</li>
</ul>
<h2>Dataset</h2>
<p>The images used for face recognition are stored in the <code>database</code> directory. The directory structure is as follows:</p>
<pre class="code-block-wrapper"><div class="code-block-header"><span class="code-block-header__lang"></span><span class="code-block-header__copy"></span></div><code class="hljs code-block-body ">database
├── perso<span class="hljs-symbol">n1</span>
│   ├── perso<span class="hljs-symbol">n1</span>_<span class="hljs-number">1.</span>jpg
│   └── perso<span class="hljs-symbol">n1</span>_<span class="hljs-number">2.</span>jpg
└── perso<span class="hljs-symbol">n2</span>
    └── perso<span class="hljs-symbol">n2</span>_<span class="hljs-number">1.</span>jpg
</code></pre>
<p>To use your own images, simply add them to the corresponding <code>person</code> subdirectory.</p>
<h2>Usage</h2>
<p>To use this project, place your images in the <code>database/person</code> directory and run the corresponding Python script.</p>
</div>
