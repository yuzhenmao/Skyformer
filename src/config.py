Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@yuzhenmao 
yuzhenmao
/
Skyformer
Public
forked from pkuzengqi/Skyformer
Fork your own copy of yuzhenmao/Skyformer
Code
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Skyformer
/
src
/
config.py
in
main
 

Spaces

2

No wrap
1
​
2
​
3
# seq_len=4096, nb_feat=256
4
# seq_len=512, nb_feat=64
5
### big bird: n*nbf = (r+w+g)*b*n, block_size = nb_feat / 10
6
​
7
listops = {
8
              "dataset":{
9
                  "train":96000,
10
                  "dev":2000,
11
                  "test":2000,
12
              },
13
              "model":{
14
                  "learn_pos_emb":True,
15
                  "tied_weights":False,
16
                  "embedding_dim":512, 
17
                  "transformer_dim":512, 
18
                  "transformer_hidden_dim":1024, 
19
                  "head_dim":512, 
20
                  "num_head":2, 
21
                  "num_layers":2,
22
                  "vocab_size":32,
23
                  "max_seq_len":8000,
24
                  "dropout_prob":0.1,
25
                  "attention_dropout":0.1,
26
                  "pooling_mode":"MEAN",
27
                  "num_classes":10,
28
              },
29
              "training":{
30
                  "batch_size":8, 
31
                  "learning_rate":0.0001,
32
                  "warmup":1000,
33
                  "lr_decay":"linear",
34
                  "weight_decay":0,
35
                  "eval_frequency":500, 
36
                  "num_train_steps":50000,
37
                  "num_init_steps":1000,
38
                  "num_eval_steps":62,
39
                  "patience":10, 
40
              },
41
              "extra_attn_config":{
42
                  "softmax":{"bz_rate":1,},
43
                  "softmaxRBF32":{"bz_rate":1},
44
                  "kernelized":{"bz_rate":1},
45
​
@yuzhenmao
Commit changes
Commit summary
Create config.py
Optional extended description
Add an optional extended description…
 Commit directly to the main branch.
 Create a new branch for this commit and start a pull request. Learn more about pull requests.
 
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
