#!/usr/bin/python

import glob as gb
import os
import shutil as shut
#import PyV8

listin = gb.iglob('./source/*.htm')

""" def beeline(filein)
    ctxt = PyV8.JSContext()
    ctxt.enter()
    js = "
    function(){
        readStyle='style-ebook';
        readSize='size-large';
        readMargin='margin-x-narrow';
        _readability_script=document.createElement('SCRIPT');
        _readability_script.type='text/javascript';
        _readability_script.src='http://www.beelinereader.com/beelinereader/readability.js?x='+Math.random();
        document.getElementsByTagName('head')[0].appendChild(_readability_script);
        _readability_css=document.createElement('LINK');
        _readability_css.rel='stylesheet';
        _readability_css.href='http://www.beelinereader.com/beelinereader/readability.css';
        _readability_css.type='text/css';
        _readability_css.media='all';
        document.getElementsByTagName('head')[0].appendChild(_readability_css);
        _readability_print_css=document.createElement('LINK');
        _readability_print_css.rel='stylesheet';
        _readability_print_css.href='http://www.beelinereader.com/beelinereader/readability_print.css';
        _readability_print_css.media='print';
        _readability_print_css.type='text/css';
        document.getElementsByTagName('head')[0].appendChild(_readability_print_css);
    }();
    "

    js2 = "
    function(){
        var w=window,u='http://www.beelinereader.com/BlackNavyCrimson',l=w.location,d=w.document,s=d.createElement('script'),e=encodeURIComponent,x='undefined';
        function g(){
            if(d.readyState&&d.readyState!='complete'){setTimeout(g,2500);
            }else{if(typeof MainApp==x){
            s.setAttribute('src',u+'.js');
            d.body.appendChild(s);
            }
            function f(){if(typeof MainApp==x){setTimeout(f,2500)}else{MainApp.show();}}
            f();
            }
        }
       g();
    }()
    "
    ctxt.eval(js)
    ctxt.eval(js2)
"""

while True:
    #filein = open(listin.next())
    #fileout = beeline(filein)
    #save(fileout)
    try:
        orig = listin.next();
        shut.copy2(orig,orig[:-4]+'_2'+orig[-4:])
    except StopIteration
        break
