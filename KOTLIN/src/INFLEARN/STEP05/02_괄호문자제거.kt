package INFLEARN.STEP05

import java.util.*


// https://cote.inflearn.com/contest/10/problem/05-02
// 괄호사이의 문자를 모두 제거 후 출력
/*
in
(A(BC)D)EF(G(H)(IJ)K)LM(N)

out
EFLM
*/

private fun solution(str: String): String? {
    var answer = ""
    val stack = Stack<Char>()
    for (x in str.toCharArray()) {
        if (x == ')') {
            while (stack.pop() != '(');
        } else stack.push(x)
    }
    for (i in stack.indices) answer += stack[i]
    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val str = kb.next()
    println(solution(str))
}