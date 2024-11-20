from scripts.memenager import MemMenager
from flask import render_template, Flask

mm = MemMenager()
app = Flask(__name__)


@app.route('/')
def index():
    limits = [6, 3, 3, 9, 3, 3]
    page_limits = {
        "jbzd_limit": limits[0],
        "jm_limit": limits[1],
        "dm_limit": limits[2],
        "kw_limit": limits[3],
        "rm_limit": limits[4],
        "ag_limit": limits[5]
    }

    mm.fresh_mems(page_limits, 60 * 5)

    jebmem = mm.memy['jebmem'] if 'jebmem' in mm.memy.keys() else {}
    jebvmem = mm.memy['jebvmem'] if 'jebvmem' in mm.memy.keys() else {}
    urljm = mm.memy['urljm'] if 'urljm' in mm.memy.keys() else {}
    demomemp = mm.memy['demomemp'] if 'demomemp' in mm.memy.keys() else {}
    demomemv = mm.memy['demomemv'] if 'demomemv' in mm.memy.keys() else {}
    kwmems = mm.memy['kwmems'] if 'kwmems' in mm.memy.keys() else {}
    rmmems = mm.memy['rmmems'] if 'rmmems' in mm.memy.keys() else {}
    agmems = mm.memy['agmems'] if 'agmems' in mm.memy.keys() else {}

    return render_template('sec_template.html',
                           jebmem=jebmem,
                           jebvmem=jebvmem,
                           urljm=urljm,
                           demomemp=demomemp,
                           demomemv=demomemv,
                           kwmems=kwmems,
                           rmmems=rmmems,
                           agmems=agmems,
                           title='only for you :)')
