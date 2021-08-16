package STEP05

import java.util.*


// https://cote.inflearn.com/contest/10/problem/05-04
// 후위식 연산 출력
/*
in
352+*9-

out
12
*/

private fun solution(str: String): Int {
    var answer = 0
    val stack = Stack<Int>()
    for (x in str.toCharArray()) {
        if (Character.isDigit(x)) {
            stack.push(x.toInt() - 48)
        } else {
            val rt = stack.pop()
            val lt = stack.pop()
            if (x == '+') stack.push(lt + rt)
            else if (x == '-') stack.push(lt - rt)
            else if (x == '*') stack.push(lt * rt)
            else if (x == '/') stack.push(
                lt / rt
            )
        }
    }
    answer = stack[0]
    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val str = kb.next()
    println(solution(str))
}