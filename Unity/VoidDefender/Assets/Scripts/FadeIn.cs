using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class FadeIn : MonoBehaviour
{
	public float fadeTime = 5f;          // Speed that the screen fades to and from black.
	

	private bool fadeIn;
	private Image fadePanel;
	private Color currentColor;

	//Alternative to the fade in animation
	void Start() {
		fadePanel = GetComponent<Image>();
		currentColor = Color.black; //if we want to be able to edit the level, we only active fade on start

	}

	void Update() {
		if (Time.timeSinceLevelLoad < fadeTime)	{
			//fade in
			//currentColor.a = 1 - (Time.timeSinceLevelLoad/ fadeTime);
			//fadePanel.color = currentColor;//how I did it
			float alphaChange = Time.deltaTime / fadeTime;

			currentColor.a -= alphaChange;

			fadePanel.color = currentColor;
		}
		else {
			gameObject.SetActive(false);
		}
	}



	void FadeToClear()
	{
		fadePanel.CrossFadeAlpha(0.0f, 0.05f, false);
	}
}
