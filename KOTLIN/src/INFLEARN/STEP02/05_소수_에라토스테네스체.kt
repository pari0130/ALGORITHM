package INFLEARN.STEP02

import java.util.*


// https://cote.inflearn.com/contest/10/problem/02-05
// 만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
/*
    in
    20

    out
    8
*/
private fun solution(n: Int): Int {
    var answer = 0
    val ch = IntArray(n + 1)

    for (i in 2..n) {
        if (ch[i] == 0) {
            answer++
            for(j in i..n step i){
                ch[j] = 1
            }
//            var j = i
//            while (j <= n) {
//                j += i
//                if (j > n) break
//                else ch[j] = 1
//            }
        }
    }

    println(ch.toString())

    return answer
}

fun main() {
    val kb = Scanner(System.`in`)
    val n = kb.nextInt()

    println(solution(n))
}