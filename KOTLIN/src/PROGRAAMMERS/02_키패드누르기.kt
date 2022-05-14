package PROGRAAMMERS

import java.lang.Math.abs
import java.lang.Math.sqrt
import java.util.logging.Logger
import kotlin.math.pow
import kotlin.math.round

// https://programmers.co.kr/learn/courses/30/lessons/67256?language=kotlin

fun main() {
//    val kb: Scanner = Scanner(System.`in`)
//    val numbers1 = intArrayOf(kb.next().toInt())
//    val hand1 = kb.next()

    val numbers = intArrayOf(1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5) // LRLLLRLLRRL
    // val numbers = intArrayOf(7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2) // LRLLRRLLLRR
    // val numbers = intArrayOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 0) // LLRLLRLLRL
    val hand = "right" // right left
    val solution = solution(numbers, hand) // LRLLLRLLLRL

    println(solution)

    if(solution == "LRLLLRLLRRL") {
        println("true")
    } else {
        println("false")
    }
}

private fun solution(numbers: IntArray, hand: String): String {
    var answer = ""
    val hands = mapOf("left" to "L", "right" to "R")
    val pad = listOf(
        intArrayOf(1, 2, 3),
        intArrayOf(4, 5, 6),
        intArrayOf(7, 8, 9),
        intArrayOf(-1, 0, -1)
    )
    val leftNumbers = intArrayOf(1, 4, 7)
    val rightNumbers = intArrayOf(3, 6, 9)
    // val dmzNumbers = intArrayOf(0, 0, 0)
    var leftPos = intArrayOf(3, 0)
    var rightPos = intArrayOf(3, 2)
    var curPos: IntArray

    for (i in 0..numbers.lastIndex) {
        curPos = getPos(pad, numbers[i])

        println("왼손위치 pos -> ${numbers[i]}, ${leftPos.toList()}")
        println("오른손위치 pos -> ${numbers[i]}, ${rightPos.toList()}")
        println("가야할위치 pos -> ${numbers[i]}, ${curPos.toList()}")

        if (numbers[i] in leftNumbers) {
            answer += hands["left"]
        } else if (numbers[i] in rightNumbers) {
            answer += hands["right"]
        } else { // 2,5,8,0
            answer += if (getPosDistance(leftPos, curPos) < getPosDistance(rightPos, curPos)) {
                // 왼손 거리가 더 가까울 경우
                hands["left"]
            } else if (getPosDistance(rightPos, curPos) < getPosDistance(leftPos, curPos)) {
                // 오른손 거리가 더 가까울 경우
                hands["right"]
            } else {
                // 거리가 같을 경우
                hands[hand]
            }
        }

        if (answer.last().toString() == hands["left"]) {
            leftPos = curPos
        } else if (answer.last().toString() == hands["right"]) {
            rightPos = curPos
        }
    }

    return answer
}

private fun getPos(pad: List<IntArray>, number: Int): IntArray {
    for (i in 0..pad.lastIndex) {
        for (j in 0..pad[i].lastIndex) {
            if (pad[i][j] == number) {
                println("$i, $j")
                return intArrayOf(i, j)
            }
        }
    }
    return intArrayOf()
}

/*
* println("5, 8 -> ${getPosDistance(intArrayOf(1,1), intArrayOf(2,1))}")
* println("3, 8 -> ${getPosDistance(intArrayOf(0,2), intArrayOf(2,1))}")
* */
private fun getPosDistance(last: IntArray, current: IntArray): Int {
    val lx = last[0]
    val ly = last[1]
    val tx = current[0]
    val ty = current[1]
    return (kotlin.math.abs(tx - lx) + kotlin.math.abs(ty - ly))
}

// 두 좌표 절대값 계산
fun getDistance(x: Int, y: Int, x1: Int, y1: Int): Double {
    // Math.pow() <- 제곱
    // Math.sqrt() <- 루트
    val d: Double
    val xd: Int
    val yd: Int
    yd = Math.pow((y1 - y).toDouble(), 2.0).toInt()
    xd = Math.pow((x1 - x).toDouble(), 2.0).toInt()
    d = sqrt((yd + xd).toDouble())
    // return round(sqrt((last[1]-target[1]).toDouble().pow(2) + (last[0]-target[0]).toDouble().pow(2)))
    //return kotlin.math.sqrt(last[1]-target[1].toDouble().pow(2.0) + last[0]-target[0].toDouble().pow(2.0))
    return d
}

/*
* 4	2 5	R	왼손 거리와 오른손 거리가 1로 같으므로, 오른손으로 5를 누릅니다.
* 4	9 5	L	왼손 거리는 1, 오른손 거리는 2이므로 왼손으로 5를 누릅니다.
*
* 4 == 1,0 / 9 == 2,2 / 누를 숫자  5 == 1,1
*
*
* 3, 1
왼손위치 pos -> 0, [2, 0]
오른손위치 pos -> 0, [2, 3]
가야할위치 pos -> 0, [3, 1]
*
* */