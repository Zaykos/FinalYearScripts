import time
from mods import chckurl
from mods import chckwaf
from mods import multi_index
from mods import hdrchck
from mods.cms import wp
from mods import dnsfuzz
from mods import apch
from mods import errorsing
from mods import bup
from mods import gitexp
def main(url,urlht,ver):

    time1 = time.time()
    header = {"User-Agent": "Venera/1.0"}

    print("""\033[1;33mTarget\033[0;0m: {} - {}""".format(url,urlht))
    chckurl.check(urlht,header)
    chckwaf.checkwaf(urlht,header)
    multi_index.multi_index(url,header)
    errorsing.errorsig(url,header)
    hdrchck.header(urlht,header)

    wp.wp(urlht, header)

    dnsfuzz.dnsfuzz(url,header)
    apch.apache_(urlht,header)
    bup.backup(url,header)
    gitexp.git_exposed(url,header)


    time2 = time.time()
    time0 = time2 - time1
    time4 = str(time0)
    time4 = time4.split(".")
    time5 = time4[0]
    t = """
The scan took {} seconds.
    """.format(time5)
    print(t)
