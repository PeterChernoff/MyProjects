﻿using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class PlanetWin : MonoBehaviour {

	public Sprite[] sprites;
	private Image planetSprite;

	// Use this for initialization
	void Start ()
	{
		planetSprite = GetComponentInChildren<Image>();
		int randomize = Random.Range(0, sprites.Length);
		planetSprite.sprite = sprites[randomize];

	}
}
