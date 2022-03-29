#!/usr/bin/env python3
from subprocess import run
from time import sleep

psizes = ["2000", "5000"]

#psizes = ["250"]

fsizes = ["20k"]
#fsizes = ["1k"]


cmds = {
"gpu_blr": "python app/main.py run gpu_blr inputs/Arand{fsize}.mat.npy inputs/xrand{fsize}.mat.npy {partsize}",
"2gpu_blr": "CUDA_VISIBLE_DEVICES=0,1 python app/main.py run mgpu_blr inputs/Arand{fsize}.mat.npy inputs/xrand{fsize}.mat.npy {partsize}",
"4gpu_blr": "python app/main.py run mgpu_blr inputs/Arand{fsize}.mat.npy inputs/xrand{fsize}.mat.npy {partsize}",

"parla_1gpu": "CUDA_VISIBLE_DEVICES=0 python app/main.py run parla inputs/Arand{fsize}.mat.npy inputs/xrand{fsize}.mat.npy {partsize}",
"parla_2gpu": "CUDA_VISIBLE_DEVICES=0,1 python app/main.py run parla inputs/Arand{fsize}.mat.npy inputs/xrand{fsize}.mat.npy {partsize}",
"parla_4gpu": "python app/main.py run parla inputs/Arand{fsize}.mat.npy inputs/xrand{fsize}.mat.npy {partsize}",
}

#parla_plac = ["sched", "manual"]
parla_plac = ["manual"]
parla_data = ["eager", "lazy"]

for fsize in fsizes:
    for psize in psizes:
        for name, cmd in cmds.items():
            fname = f"{name}_p{psize}"
            cmd = cmd.format(partsize=psize, fsize=fsize)

            if "parla" not in name:
                print("running  ", cmd)
                with open(fname+".dat", "w") as outfile:
                    #pass
                    run(cmd, shell=True, stdout=outfile)
            else:
                for pp in parla_plac:
                    for pd in parla_data:
                        cmd = cmd + f" {pd} {pp}"
                        fname = fname + f"_{pd}_{pp}"
                        print("running  ", cmd)
                        with open(fname+".dat", "w") as outfile:
                            pass
                            run(cmd, shell=True, stdout=outfile)
                            sleep(2)
            sleep(2)
