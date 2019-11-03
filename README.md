# Expected-weight-of-minimum-spanning-tree
Randomized Algorithm project_04

实现一种随机图，在随机图上实现对最小生成树的抽样过程，由抽样过程实现蒙特卡罗方法计算最小生成树权值的数学期望估计，比较估计结果的准确性。理解蒙特卡罗算法的过程和效用，体会由经验公式得到理论公式的过程。  
1.实现算法产生n顶点随机图的生成；  
输入：n  
输出：一个n顶点随机图，任意两个顶点之间边的权值均匀分布于(0,1)  
2.调用第1步实现的算法，实现对n顶点图的均匀抽样；   
3.在抽样样本上计算最小生成树并计算其权值的数学期望（使用了Prim算法）；  
4.在第2步第3步的基础上，建立n与最小生成树权值数学期望间的关系；  
5.对n=16,32,64,128,256,512,1024…展开实验，考察算法运行时间的变化，并检验所建立的关系的一般性；  
6.尝试用理论分析解释实验结果
