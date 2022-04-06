package INFLEARN.STEP01

import java.lang.StringBuilder
import java.util.Scanner

// 각각의 문자가 입력받은 target 으로 부터 떨어진 거리 index 를 구해서 return
// teachermode e : 1 0 1 2 1 0 1 2 2 1 0
fun main() {
    val kb: Scanner = Scanner(System.`in`)
    val str = kb.next()
    val c = kb.next().get(0)

    for (x in solution(str, c)) {
        print("$x ")
    }
}

private fun solution(s: String, t: Char): IntArray {
    val answer = IntArray(s.length)
    var p = 1000

    // indices : 0..length - 1
    for (i in s.indices) {
        if (s.get(i) == t) {
            p = 0
            answer[i] = p
        } else {
            p++
            answer[i] = p
        }
    }

    p = 1000
    // lastIndex : this.length - 1
    for (i in s.lastIndex downTo 0) {
        if (s.get(i) == t) {
            p = 0
        } else {
            p++
            //#팁 Math.min(1, 2) 작은 숫자 비교
            answer[i] = answer[i].coerceAtMost(p)
        }
    }

    return answer
}