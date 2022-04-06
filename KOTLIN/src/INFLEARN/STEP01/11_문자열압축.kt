package INFLEARN.STEP01

import java.lang.StringBuilder
import java.util.Scanner

// 문자열 압축,
// KKHSSSSSSSE : K2HS7E
fun main() {
    val kb: Scanner = Scanner(System.`in`)
    val str = kb.next()
    println(solution(str))

}

private fun solution(str: String): String {
    val answer = StringBuilder()
    val s = "$str "
    var cnt = 1

    for (i in str.indices) {
        if (s.get(i) == s.get(i + 1)) {
            cnt++
        } else {
            answer.append(s.get(i))
            if (cnt > 1) {
                answer.append(cnt.toString())
            }
            cnt = 1
        }
    }
    return answer.toString()
}