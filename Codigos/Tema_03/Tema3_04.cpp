//C++ code

void tree(double branchLen, Turtle t) {
    //Compare with ActiveCode 1
    if (branchLen > 5) {
            t.forward(branchLen);
            t.right(20);
            tree(branchLen - 15, t);
            t.left(40);
            tree(branchLen - 15, t);
            t.right(20);
            t.forward(-branchLen);
    }
}



