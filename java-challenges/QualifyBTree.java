
import java.util.Scanner;

public class QualifyBTree {
    static class BTree{
        public BTree(String node){ this.node = node; }
        String node;
        BTree L = null;
        BTree R = null;
    }
    static BTree initBTree(){
        BTree t = new BTree("finais");
        
        t.L = new BTree("semi-finais");
        t.R = new BTree("semi-finai");
        
        t.L.L = new BTree("quartas de finais");
        t.L.R = new BTree("quartas de finais");
        t.R.L = new BTree("quartas de finais");
        t.R.R = new BTree("quartas de finais");

        t.L.L.L = new BTree("oitavas de finais");
        t.L.L.R = new BTree("oitavas de finais");
        t.L.R.L = new BTree("oitavas de finais");
        t.L.R.R = new BTree("oitavas de finais");
        t.R.L.L = new BTree("oitavas de finais");
        t.R.L.R = new BTree("oitavas de finais");
        t.R.R.L = new BTree("oitavas de finais");
        t.R.R.R = new BTree("oitavas de finais");

        t.L.L.L.L = new BTree("1");
        t.L.L.L.R = new BTree("2");
        t.L.L.R.L = new BTree("3");
        t.L.L.R.R = new BTree("4");
        t.L.R.L.L = new BTree("5");
        t.L.R.L.R = new BTree("6");
        t.L.R.R.L = new BTree("7");
        t.L.R.R.R = new BTree("8");
        t.R.L.L.L = new BTree("9");
        t.R.L.L.R = new BTree("10");
        t.R.L.R.L = new BTree("11");
        t.R.L.R.R = new BTree("12");
        t.R.R.L.L = new BTree("13");
        t.R.R.L.R = new BTree("14");
        t.R.R.R.L = new BTree("15");
        t.R.R.R.R = new BTree("16");
        return t;
    }

    static boolean isHere(String node, BTree root){
        if (node.equals(root.node)){
            return true;
        }else if (root.L != null && root.R != null){
            return isHere(node, root.L) || isHere(node, root.R);
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String a = in.next();
        String b = in.next();
        in.close();

        BTree t = initBTree();

        BTree aT = null;
        BTree bT = null;
        
        boolean found = false;
        while (!found){
            aT = t.R;
            bT = t.R;
            if (isHere(a, t.L))
                aT = t.L;
            if (isHere(b, t.L))
                bT = t.L;
            if (aT.equals(bT)){
                t = aT;
            }else{
                System.out.printf("Os times %s e %s encontram nas %s\n", a, b, t.node);
                found = true;
            }
        }
    }
}
