#!/usr/bin/env python
"""
    To run from the command line, specify the two file names
    as paramaters.
"""
import sys
from PIL import Image

def compare(filename_a, filename_b):
    """
    Compare the two image files, and compute the distance between them.
    """
    imga = Image.open(filename_a)
    imgadata = imga.getdata()
    imgb = Image.open(filename_b)
    imgbdata = imgb.getdata()

    score = 0L
    total_wrong = 0L

    for ya in range(350, 351): # TODO: compare more than just one row
        yb = ya
        # setup levenshtien d matrix initials
        am = imga.size[0]
        bm = imgb.size[0]
        grid = [ [0] * (bm+1) ] * (am+1)
        for i in range(1, am+1):
            grid[i][0] = i+1
        for i in range(1, bm+1):
            grid[0][i] = i+1
        # go through each pixel
        for xa in range(1, am+1):
            for xb in range(1, bm+1):
                coorda = (imga.size[0]*(ya-1))+(xa-1)
                coordb = (imga.size[0]*(yb-1))+(xb-1)
                pixa = imgadata[coorda][0:3]
                pixb = imgbdata[coordb][0:3]
                pixd = abs(pixa[0] - pixb[0])
                pixd += abs(pixa[1] - pixb[1])
                pixd += abs(pixa[2] - pixb[2])
                pixd /= 3
                # make threshold 1/16
                if pixd / 16:
                    grid[xa][xb] = grid[xa-1][xb-1]
                else:
                    ddel = grid[xa-1][xb] + 1
                    dins = grid[xa][xb-1] + 1
                    # cost = 2, because you have to del and ins
                    dsub = grid[xa-1][xb-1] + 1
                    grid[xa][xb] = min(ddel, dins, dsub)
        score += grid[am][bm]
        total_wrong += am * bm
    return score, total_wrong

def main():
    """ run from the console """
    distance, total = compare(sys.argv[1], sys.argv[2])
    sys.stdout.write("levenshtein distance: %d error: %f%%\n"
                     % (distance, (float(distance) / float(total))*100.))

if __name__ == '__main__':
    main()
