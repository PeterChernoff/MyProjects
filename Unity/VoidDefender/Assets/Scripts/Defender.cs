using UnityEngine;
using System.Collections;

[RequireComponent(typeof(Health))]
public class Defender : Creature
{
	public int starCost = 100;
	

	[SerializeField]
	private string nameOfDefender;

	public string GetName()
	{
		return nameOfDefender;
	}
	
	//using this as a tag for now
	// Use this for initialization
	void Start () {
		gameObject.layer = LayerMask.NameToLayer("Defender");

	}
	public int GetStarCost()
	{
		return starCost;
	}
	
}
