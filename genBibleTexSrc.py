import os
os.system("clear") ;
os.system("cat bible_out/prefix   > bible_out/bible.tex") ;
# ----------------------------------
# the bible source includes
# 1: cuvr;
# ----------------------------------
fp_index    = open( "bibleIndex.txt"      , "r" )
str_index   = fp_index.readlines()
fp_index.close()
fp          = open( "bible_out/bible.tex" , "a" )
# cross referencing index to be added
# by 1 whenever there is a new section
xrefCnt     = 1
xbkCnt      = 0
for lines in str_index :
    xbkCnt += 1
    words   = lines.replace("\n","").split()
    # -------------------------------------------------------------------
    # words[0] words[1] words[2] words[3] Chi title abrev Eng title abrev
    # -------------------------------------------------------------------
    print( "----------------------------" )
    print( words[0] + " " + words[2]      )
    print( "----------------------------" )
    # -------------------
    # open the four bible
    # -------------------
    fp_cuvr = open( "bible_src/cuvr/"    + words[3] + ".txt" ) ; content_cuvr = fp_cuvr.readlines() ; fp_cuvr.close()
    # -----------------------------------------------------
    # [ GEN LATEX ] : create \chapter{} for current segment
    # -----------------------------------------------------
    print( words[0]+words[2] )
    fp.write( "\\section{"+words[0]+" "+words[2]+"}\n" )
    fp.write( "\\label{subsec:book"+str(xbkCnt)+"}\n"  )
    #fp.write( "\\begin{multicols}{2}\n"                )
    #fp.write( "\\tableofcontent\n"                            )
    #fp.write( "\\end{multicols}\n"                     )
    # ------------------------------------------
    # check total chapter number in this segment
    # ------------------------------------------
    # -------
    # cuvr
    # -------
    sentenceNum = len( content_cuvr )
    print("sentence no. in cuvr "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_cuvr[ sentenceNum - 1 ].split(".")[0] )
    print("cuvr "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -----------------------------
    # check sentenceNum per chapter
    # -----------------------------
    sentenceNumPerChapter = {}
    #colorIntensity        = 15
    colorIntensity        = 100
    colorArr              =['CUV1LightRed'   , \
                            'LZZVLightGray'  , \
                            'KJVVLightGreen' , \
                            'CUV2LightYellow', \
                            'CNVVLightBrown' , \
                            'NRSVLightBlue'  , \
                            'WENLLightPurple']
    for chapterIdx in range(1,chapterNum+1,1) :
        if chapterIdx > 1:
            fp.write("\\newpage\n");
        # <<<< when a new version is added, no. of "c" in tabular requires adjustment >>>>
        bibleStr = "\subsection{"+words[0]+" "+words[2]+" "+str(chapterIdx)+"}" \
                   +"\\label{sec:"+str(xrefCnt)+"}"                              \
                   +" \hyperlink{toc}{[返主目录]}"\
                   +"\n"
        fp.write( bibleStr )
        #fp.write( "\\newline\n" )
        fp.write( "\\hyperref[sec:"+str(xrefCnt-1)+"]{< < < 上一章 < < <} ~~~ \\hyperref[sec:"+str(xrefCnt+1)+"]{> > > 下一章 > > >} \\newline \n" )
        xrefCnt += 1
        for sentenceIdx in range(0,sentenceNum,1) :
            if ( chapterIdx < 10 and int(content_cuvr[sentenceIdx].split(".")[0]) == chapterIdx ) or \
               ( chapterIdx > 9  and int(content_cuvr[sentenceIdx].split(".")[0]) == chapterIdx ) :
                #bibleStr = "\\begin{tabularx}{\\textwidth}{|c|X|}\n"  ; fp.write( bibleStr )
                bibleStr = "\\begin{tabularx}{\\textwidth}{cX}\n"  ; fp.write( bibleStr )
                #bibleStr = "\hline\n"                                 ; fp.write( bibleStr )
                bibleStr = content_cuvr[sentenceIdx].replace("\n","")
                bibleStr = bibleStr.split(" ",1)
                # <<<< when a new version is added, argument in "multirow" requires adjustment >>>>
                bibleStr1= bibleStr[0] ; fp.write( bibleStr1)
                # ---------------------------------------------------
                # add the content of cuvr to 1st row
                # ---------------------------------------------------
                bibleStr2= " & "+bibleStr[1]+" \\\\\n" ; fp.write( bibleStr2)
                # ---------------------------------------------------
                # end current sentence
                # ---------------------------------------------------
                #bibleStr = "\hline\n"                                 ; fp.write( bibleStr )
                bibleStr = "\end{tabularx}\n"                         ; fp.write( bibleStr )
fp.close()
#os.system("cat bible_out/afterword >> bible_out/bible.tex")
os.system("cat bible_out/postfix >> bible_out/bible.tex")
