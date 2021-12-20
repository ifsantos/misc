import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class QualifyBTree {
    static class BTree{
        public BTree(String node){ this.node = node; }
        String node;
        BTree L = null;
        BTree R = null;
        /*
        public boolean equals(BTree t){
            return this.node.equals(t.node);
        }
        */
    }
    static BTree initBTree(){
        BTree t = new BTree("final");
        
        t.L = new BTree("semi-final");
        t.R = new BTree("semi-final");
        
        t.L.L = new BTree("quartas de final");
        t.L.R = new BTree("quartas de final");
        t.R.L = new BTree("quartas de final");
        t.R.R = new BTree("quartas de final");

        t.L.L.L = new BTree("oitavas de final");
        t.L.L.R = new BTree("oitavas de final");
        t.L.R.L = new BTree("oitavas de final");
        t.L.R.R = new BTree("oitavas de final");
        t.R.L.L = new BTree("oitavas de final");
        t.R.L.R = new BTree("oitavas de final");
        t.R.R.L = new BTree("oitavas de final");
        t.R.R.R = new BTree("oitavas de final");

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

        Map<String, BTree> nodeTree = new HashMap<String,BTree>();
        
        boolean found = false;
        while (!found){

            if (isHere(a,t.L)){
                nodeTree.put(a, t.L);
            }else if (isHere(a,t.R)){
                nodeTree.put(a, t.R);
            }
            if (isHere(b,t.L)){
                nodeTree.put(b, t.L);
            }else if (isHere(b,t.R)){
                nodeTree.put(b, t.R);
            }

            if (nodeTree.get(b).equals(nodeTree.get(a))){
                t = nodeTree.get(b);
            }else{
                System.out.printf("Se %s e %s encontraram em %s", a, b, t.node);
                found = true;
            }
        }
    }
}
