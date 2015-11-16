
<pre>
convert.py  -- change the origin data into features, hashvalue and c-Signature
  |___hash.txt : output hash value
  |___cSig.txt : output cSig value
  |___feature.txt : extracted features

Tree.py -- build the c tree
  |___ tree0.txt - 第一列是hashID 后面是对应的set
  |___ treeO_x.txt - x: hashID为x对应的文件 第一列是insID（样例的ID）后面是T1-T5的label

query_id - 所有＋1label的数据

<pre>
