#2 binary trees: find if same set of unique elements
"""
One method is Recursion
    add_element(key)

    p_node = find_parent(node, key)
        if(key < node.data && node.left)
            return f_p(node.left, key)



    find_parent(n, k){
        if n.data > k {
            if n.left{
                return f_p(n.left, k)
                }
            else{
                return n
                }
        }
        if (n.data < k) {
            if (n.right) {
                return f_p(n.right, k)}
            else{
                return n }
        }



    add_node_r(key):
        if isEmpty(){
            treeNode = TreeNode(key)
            root = treeNode }
        else{
            newNode = TreeNode(key)
            p_node = find_parent(root, key)
            if p_node.data > key {
                p_node.left = newNode
                newNode.parent = p_node }
            elif p_node.data < key {
                p_node.right = newNode
                newNode.parent = p_node }
            else {
                
