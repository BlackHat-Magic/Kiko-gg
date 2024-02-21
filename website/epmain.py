from flask import Blueprint, Flask, render_template, redirect, url_for, request, flash, jsonify
import json

epmain = Blueprint("epmain", __name__)

@epmain.route("/")
def home():
    return(
        render_template(
            "index.html",
            title="Home"
        )
    )

@epmain.route("/yt")
@epmain.route("/youtube")
def youtube():
    return(
        redirect(
            "https://www.youtube.com/@AlgoraKiko"
        )
    )

@epmain.route("/t")
@epmain.route("/x")
@epmain.route("/twt")
@epmain.route("/twitter")
def twitter():
    return(
        redirect(
            "https://twitter.com/AlgoraKiko"
        )
    )

@epmain.route("/ttv")
@epmain.route("/twitch")
def twitch():
    return(
        redirect(
            "https://twitch.tv/AlgoraKiko"
        )
    )

@epmain.route("/discord")
def discord():
    return(
        redirect(
            "https://discord.com/invite/cFVFG26"
        )
    )

@epmain.route("/insta")
@epmain.route("/instagram")
def instagram():
    return(
        redirect(
            "https://www.instagram.com/algorakiko/"
        )
    )

@epmain.route("/tiktok")
def tiktok():
    return(
        redirect(
            "https://www.tiktok.com/@algorakiko"
        )
    )

@epmain.route("/spotify")
def spotify():
    return(
        redirect(
            "https://open.spotify.com/user/jailenetalampas"
        )
    )