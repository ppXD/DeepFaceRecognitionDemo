<div class="markdown-body"><h1>Face Recognition</h1>
<p>This project is a demo showcasing facial recognition using deep learning, based on the <a href="https://github.com/serengil/deepface">deepface</a> repository.</p>
<h2>Dependencies</h2>
<p>The following dependencies are required to run this project:</p>
<ul>
<li>tensorflow</li>
<li>deepface</li>
</ul>
<p>You can install them using <code>pip</code>:</p>
<pre class="code-block-wrapper"><div class="code-block-header"><span class="code-block-header__lang"></span><span class="code-block-header__copy"></span></div><code class="hljs code-block-body ">pip <span class="hljs-keyword">install</span> tensorflow
pip <span class="hljs-keyword">install</span> deepface
</code></pre>
<h2>Usage</h2>
<p>The <code>database</code> directory is used to store the facial data that you want to recognize. The structure of the directory should be as follows:</p>
<pre class="code-block-wrapper"><div class="code-block-header"><span class="code-block-header__lang"></span><span class="code-block-header__copy"></span></div><code class="hljs code-block-body ">database
    person_name
        person1.<span class="hljs-keyword">jpg
</span>    other_person_name
        other_person1.<span class="hljs-keyword">jpg
</span></code></pre>
<p>The <code>face_rec_find.py</code> script supports recognition of multiple faces, while <code>face_rec_verify.py</code> supports recognizing a single face.</p>
<p>By default, <code>face_rec_find.py</code> uses the <code>database</code> directory for facial recognition. Simply add your photos to the appropriate subdirectories and run the script.</p>
<p>To use <code>face_rec_verify.py</code>, modify the <code>reference_img</code> variable inside the script with the path to your photo, and then run it.</p>
</div>
