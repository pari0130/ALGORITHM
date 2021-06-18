package STEP01

import java.lang.StringBuilder
import java.util.Scanner

// 알파벳과 특수문자 들이 포함된 문자열에 대해 알파벳만 뒤집힌 문자열을 출력한다.
fun main() {
    val kb: Scanner = Scanner(System.`in`)
    val str = kb.next()
    println(solution(str))
}

private fun solution(str: String): String {
    var answer = ""
    val s = str.toCharArray()
    var lt : Int = 0
    var rt : Int = str.length

    // 알파벳 체크 : isLetter()
    while (lt < rt){
        if(!s[lt].isLetter()) lt ++
        else if(!s[rt].isLetter()) rt--
        else {
            var tmp = s[lt]
            s[lt] = s[rt]
            s[rt] = tmp
            lt ++
            rt --
        }
    }
    answer = String(s);

    return answer
}