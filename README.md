# DNS data exfiltration simulation
A simulation of the DNS traffic produced by the following DNS data exfiltration malware:
1. FrameworkPOS (https://attack.mitre.org/software/S0503/)
2. Backdoor.Win32.Denis (https://attack.mitre.org/software/S0354/)

The simulation can be used to generate DNS traffic and inject it to benign DNS traffic datasets in order to train and test models for detection of DNS data exfiltration as performed in Nadler, Asaf, Avi Aminov, and Asaf Shabtai. "Detection of malicious and low throughput data exfiltration over the DNS protocol." Computers & Security 80 (2019): 36-53.

## Citation
If you use this code for your research, please cite our [paper](https://www.sciencedirect.com/science/article/pii/S0167404818304000):

```
@article{nadler2019detection,
  title={Detection of malicious and low throughput data exfiltration over the DNS protocol},
  author={Nadler, Asaf and Aminov, Avi and Shabtai, Asaf},
  journal={Computers \& Security},
  volume={80},
  pages={36--53},
  year={2019},
  publisher={Elsevier}
}
```
