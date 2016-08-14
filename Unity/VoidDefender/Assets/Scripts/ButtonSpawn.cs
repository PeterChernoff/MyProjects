using UnityEngine;
using UnityEngine.UI;
using System.Collections;
using System.Collections.Generic;

public class ButtonSpawn : MonoBehaviour {

	public GameObject defenderPrefab;
	public static GameObject selectedDefender;

	private ButtonSpawn[] buttonArray;
	private SpriteRenderer spriteRenderer;
	private bool isSelected;
	private Text costText, infoText, currentSelectionText;

	private const string selectText =  "Current selection: ";

	// Use this for initialization
	void Start () {
		buttonArray = GameObject.FindObjectsOfType<ButtonSpawn>();//gets the buttons
		spriteRenderer = gameObject.GetComponentInChildren<SpriteRenderer>();//gets the sprites
		spriteRenderer.color = Color.black;//darkens the sprites
		isSelected = false;//sets each button to unselected

		costText = GetComponentInChildren<Text>();//gets the text of the child for the price
		if (!costText)
		{
			Debug.LogWarning("Can't find cost text");
		}
		else
		{
			//gets the cost of the defender
			string getCost = defenderPrefab.GetComponent<Defender>().starCost.ToString();
			costText.text = getCost;
		}
		currentSelectionText = GameObject.FindGameObjectWithTag("CurrentSelection").GetComponent<Text>();
		currentSelectionText.text = selectText + "None.";

		infoText = GameObject.FindGameObjectWithTag("InfoOutput").GetComponent<Text>();

	}
	
	void OnMouseDown()
	{
		SelectButton();
	}
	private void SelectButton()
	{

		foreach (ButtonSpawn thisButton in buttonArray)
		{
			isSelected = false;//deselects the button
			thisButton.GetComponentInChildren<SpriteRenderer>().color = Color.black;
			//darkens each of the selections
		}
		isSelected = true;//selects the button
		spriteRenderer.color = Color.white;
		//makes the current value the selected defenderPrefab across all values
		selectedDefender = defenderPrefab;
		currentSelectionText.text = selectText + defenderPrefab.GetComponent<Defender>().GetName();
		//clears out any lingering complaints
		infoText.text = "";

	}

}
